from password import generate_password
import pytest
import allure 

@allure.severity('CRITICAL')
@allure.tag('negative')
def test_minimum_length_exception():
    with allure.step("Проверяем появляется ли ошибка при передаче 3 в функцию"):
        with pytest.raises(ValueError):
            generate_password(3)

def test_default_length():
    assert len(generate_password()) == 8

def test_custom_length():
    length = 10
    assert len(generate_password(length)) == length

def test_uniqueness():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2

@pytest.mark.parametrize("length", [20, 50])
def test_long_passwords(length):
    assert len(generate_password(length)) == length

def test_edge_case_minimum():
    assert len(generate_password(4)) == 4

def test_edge_case_very_long():
    assert len(generate_password(100)) == 100

def test_negative_length_exception():
    with pytest.raises(ValueError):
        generate_password(-1)

def test_invalid_length_type_exception():
    with pytest.raises(TypeError):
        generate_password("ten")
