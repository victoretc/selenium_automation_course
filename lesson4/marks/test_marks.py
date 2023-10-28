import pytest
   
@pytest.mark.slow
def test_example_slow():
    # Код медленного теста
    assert 1 == 1 

@pytest.mark.fast
def test_example_fast():
    # Код быстрого теста
    assert 2 == 2 