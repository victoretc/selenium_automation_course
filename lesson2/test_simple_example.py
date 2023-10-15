import pytest
from faker import Faker

# Фикстура для создания фейкового email
@pytest.fixture
def fake_email():
    fake = Faker()
    return fake.email()

def test_email_format(fake_email):
    # Проверка, что в email есть символ '@'
    assert "@" in fake_email

    # Проверка, что email содержит точку после символа '@'
    assert "." in fake_email.split('@')[1]

    # Проверка, что email не пустой
    assert len(fake_email) > 0

