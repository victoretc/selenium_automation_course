import random
import string

def generate_password(length=8):
    if length < 4:
        raise ValueError("Пароль должен быть длиной не менее 4 символов")

    # Символы, которые можно использовать в пароле
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерация пароля
    password = ''.join(random.choice(characters) for i in range(length))
    return password
