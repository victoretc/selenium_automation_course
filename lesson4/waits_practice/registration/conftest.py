from faker import Faker 
import pytest 


@pytest.fixture
def random_email():
    faker = Faker()
    return faker.email()


