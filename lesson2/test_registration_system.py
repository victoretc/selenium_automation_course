import pytest
from registration_system import RegistrationSystem  

# Фикстура для инициализации системы перед каждым тестом
@pytest.fixture
def init_system():
    system = RegistrationSystem()
    yield system
    system.delete_all_users()  # постусловие: очистка базы данных после теста

def test_registration_without_pre_post_conditions():
    # Шаги тест кейса 001
    system = RegistrationSystem()
    system.register("Алекс", "alex@example.com", "+1234567890")
    users = system.view_all_users()
    assert "alex@example.com" in users  # Ожидаемый результат

def test_registration_with_pre_post_conditions(init_system):
    # Шаги тест кейса 002
    init_system.register("Алекс", "alex@example.com", "+1234567890")
    users = init_system.view_all_users()
    assert "alex@example.com" in users  # Ожидаемый результат