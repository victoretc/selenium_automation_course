import pytest
@pytest.mark.parametrize("input, expected_output", [(1, 2), (2, 3), (3, 4)])
def test_add_one(input, expected_output):
    result = input + 1
    assert result == expected_output


