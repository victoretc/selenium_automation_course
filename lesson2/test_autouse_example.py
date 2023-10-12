import pytest

# Autouse 
# Пример с использованием autouse
@pytest.fixture(autouse=True)
def print_before_tests():
    print("\n--- Начало теста ---")

def test_func1():
    assert True

def test_func2():
    assert 1 == 1

def test_func3():
    assert "str" == "str"

# Пример без использования autouse
def test_func4():
    print("\n--- Начало теста без autouse ---")
    assert True

def test_func5():
    print("\n--- Начало теста без autouse ---")
    assert 1 == 1

def test_func6():
    print("\n--- Начало теста без autouse ---")
    assert "str" == "str"

