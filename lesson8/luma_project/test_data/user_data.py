from faker import Faker
fake = Faker()

first_name=fake.first_name()
last_name=fake.last_name()
email=fake.email()
password=f"sjdfj##_{fake.name()}HH{fake.email()}"


