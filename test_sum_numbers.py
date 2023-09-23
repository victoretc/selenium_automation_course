from sum_numbers import sum_numbers

def test_add_numbers():
    assert sum_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert sum_numbers(2, 2) == 5