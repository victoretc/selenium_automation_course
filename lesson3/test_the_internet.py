import base64

import pytest
from requests import get
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v118.network import Headers
from selenium.webdriver.common.log import Log

BASE_URL = "https://the-internet.herokuapp.com/"


@pytest.mark.trio
async def test_abasic_auth(driver):
    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.network.enable())

        credentials = base64.b64encode("admin:admin".encode()).decode()
        auth = {'authorization': 'Basic ' + credentials}

        await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

        driver.get('https://the-internet.herokuapp.com/basic_auth')

    success = driver.find_element(by=By.TAG_NAME, value='p')
    assert success.text == 'Congratulations! You must have the proper credentials.'


@pytest.mark.trio
async def test_cdbasic_auth(driver):
    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.network.enable())

        credentials = base64.b64encode("admin:admin".encode()).decode()
        auth = {'authorization': 'Basic ' + credentials}

        await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

        driver.get('https://the-internet.herokuapp.com/basic_auth')

    success = driver.find_element(by=By.TAG_NAME, value='p')
    assert success.text == 'Congratulations! You must have the proper credentials.'


# Например: текст, цвет, расположение, отображение, выбор чекбокса и так далее.
def test_add_remove_elements(driver, wait):
    """Создать и удалить элемент"""
    driver.get(BASE_URL + "add_remove_elements")
    pass


def basic_auth():
    credentials = base64.b64encode("admin:admin".encode()).decode()
    return {'authorization': 'Basic ' + credentials}


def test_basic_auth_cdp_endpoint(driver, wait, log):
    """Пройти базовую авторизацию - вариант cdp_endpoint"""
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': basic_auth()})
    driver.get(BASE_URL + "basic_auth")
    assert driver.find_element(By.TAG_NAME, 'p').text == 'Congratulations! You must have the proper credentials.'


@pytest.mark.trio
async def test_js_error(driver):
    driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')

    async with driver.bidi_connection() as session:
        log = Log(driver, session)

        async with log.add_js_error_listener() as messages:
            driver.find_element(by=By.ID, value='jsException').click()

        assert "Error: Not working" in messages.exception_details.exception.description


# ToDo  cdp async bidi(cdp_api) connection
@pytest.mark.trio
async def test_basic_auth_cdp_api(driver, wait, log):
    """Пройти базовую авторизацию - вариант async cdp_api"""
    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.network.enable())
        credentials = base64.b64encode("admin:admin".encode()).decode()
        auth = {'authorization': 'Basic ' + credentials}
        # sec = '{"params": {"headers": {"authorization": "Basic YWRtaW46YWRtaW4="}}}}'
        await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))
        driver.get(BASE_URL + "basic_auth")
    for entry in driver.get_log('browser'):
        print(entry)
    assert driver.find_element(By.TAG_NAME, 'p').text == 'Congratulations! You must have the proper credentials.'


def present_via_requests(url):
    r = get(url)
    return r.status_code == 200


def test_broken_images_via_requests(driver, wait):
    """Найти сломанные изображения"""
    driver.get(BASE_URL + "broken_images")
    bad_ones_lst = []
    for img in driver.find_elements(By.TAG_NAME, "img"):
        if not present_via_requests(img.get_attribute("src")):
            bad_ones_lst.append(img.get_attribute("outerHTML"))
    assert bad_ones_lst == ['<img src="asdf.jpg">', '<img src="hjkl.jpg">'], "Сломаны: " + ["", " и "][
        len(bad_ones_lst) > 1].join(bad_ones_lst)


def js_img_with_zero_natural_width(driver):
    lst = driver.execute_script("bad_lst=new Array();"
                                "Array.prototype.forEach.call(document.images,(img)=>{"
                                "if (!img.naturalWidth) bad_lst.push(img.src)});"
                                "return bad_lst;")
    return lst


def test_broken_images_via_js_natural(driver, wait):
    """Найти сломанные изображения"""
    driver.get(BASE_URL + "broken_images")

    bad_ones_lst = []
    for img in driver.find_elements(By.TAG_NAME, "img"):
        if img.get_attribute("src") in js_img_with_zero_natural_width(driver):
            bad_ones_lst.append(img.get_attribute("outerHTML"))
    assert bad_ones_lst == ['<img src="asdf.jpg">', '<img src="hjkl.jpg">'], \
        "Сломаны: " + ["", " и "][len(bad_ones_lst) > 1].join(bad_ones_lst)


def log_state_not_found(driver):
    not_found = []
    for entry in driver.get_log('browser'):
        msg = entry["message"].split(" - ")
        if msg[1] == "Failed to load resource: the server responded with a status of 404 (Not Found)":
            not_found.append(msg[0])
    return not_found


def test_broken_images_via_network_logging(driver):
    """Найти сломанные изображения"""
    driver.get(BASE_URL + "broken_images")

    not_found = log_state_not_found(driver)

    bad_ones_lst = []
    for img in driver.find_elements(By.TAG_NAME, "img"):
        if img.get_attribute("src") in not_found:
            print(img.get_attribute("src"))
            bad_ones_lst.append(img.get_attribute("outerHTML"))
    assert bad_ones_lst == ['<img src="asdf.jpg">', '<img src="hjkl.jpg">'], "Сломаны: " + ["", " и "][
        len(bad_ones_lst) > 1].join(bad_ones_lst)


def test_checkboxes(driver, wait):
    """Практика с чек боксами"""
    driver.get(BASE_URL + "checkboxes")
    # checkbox_one = driver.find_element(By.XPATH, "//form/")
    # pass


@pytest.mark.trio
async def test_set_cookie(driver, log):
    async with driver.bidi_connection() as connection:
        execution = connection.devtools.network.set_cookie(
            name="cheese",
            value="gouda",
            domain="www.selenium.dev",
            secure=True
        )

        await connection.session.execute(execution)

    driver.get("https://www.selenium.dev")
    cheese = driver.get_cookie("cheese")

    assert cheese["value"] == "gouda"


@pytest.mark.trio
async def test_performance(driver, log):
    driver.get('https://www.selenium.dev/selenium/web/frameset.html')

    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.performance.enable())

        metric_list = await connection.session.execute(connection.devtools.performance.get_metrics())

    metrics = {metric.name: metric.value for metric in metric_list}

    assert metrics["DevToolsCommandDuration"] > 0
    assert metrics["Frames"] == 12


@pytest.mark.trio
async def test_basic_auth(driver, log):
    async with driver.bidi_connection() as connection:
        await connection.session.execute(connection.devtools.network.enable())
        credentials = base64.b64encode("admin:admin".encode()).decode()
        auth = {'authorization': 'Basic ' + credentials}
        await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

        driver.get('https://the-internet.herokuapp.com/basic_auth')

    success = driver.find_element(by=By.TAG_NAME, value='p')
    assert success.text == 'Congratulations! You must have the proper credentials.'

# def test_basic_auth_cdp_endpoint(driver, wait, log):
#     """Пройти базовую авторизацию - вариант cdp_endpoint"""
#     driver.execute_cdp_cmd("Network.enable", {})
#     driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': basic_auth()})
#     driver.get(BASE_URL + "basic_auth")
#     assert driver.find_element(By.TAG_NAME, 'p').text == 'Congratulations! You must have the proper credentials.'
