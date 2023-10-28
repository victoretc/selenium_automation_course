import pytest

def load_emails():
    with open("emails.txt", "r") as f:
        return [line.strip() for line in f]

a = load_emails()
print(a)

@pytest.mark.parametrize("email", load_emails())
def test_check_at_symbol(email):
    assert "@" in email, f"Email address '{email}' does not contain '@' symbol"
