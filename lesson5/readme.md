# Пригодится

база знаний (code): <https://github.com/victoretc/helloauto>
практика с ожиданиями: <https://victoretc.github.io/selenium_waits/>
selene: <https://github.com/yashaka/selene>
база знаний (url): <https://victoretc.github.io/helloauto/>
allure-pytest (дока): <https://allurereport.org/docs/pytest/>
conftest:

<!-- import pytest
from selene import browser, support
import allure_commons
import allure

@pytest.fixture(autouse=True)
def browser_management():

    from selenium import webdriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    browser.config.driver_options = options
    browser.config.window_height = 100
    browser.config.window_width = 500

    browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )
    
    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    browser.quit() -->

Как внести свой вклад:
<!-- Как внести свой вклад?

Сделайте форк проекта: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
Клонировать свою версию проекта: git clone название_вашего_форка
Создать новую ветку для изменений: git checkout -b название_ветки
Отправить изменения в свой репозиторий
Отправить Pull Request в оригинальный репозиторий
Установка Hugo: https://gohugo.io/installation/

Основные моменты:

Установка Hugo: https://gohugo.io/installation/
Существующие посты можно найти в папке content/posts/
Создать новый пост: hugo new posts/name_of_posts.md
В каждом посте есть комментарии, которые начинаются с TODO. Пример

Можно исправить некоторые моменты в соответствии с комментариями. Так же можно оставлять свои предложения. -->