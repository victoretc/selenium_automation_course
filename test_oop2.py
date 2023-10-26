import math

from selenium import webdriver
from selenium.webdriver.common.by import By


# == Пример с геометрическими фигурами ==
# Базовый класс
class Shape:
    def area(self):  # Абстрактный метод "площадь фигуры"
        pass

    def perimeter(self):  # Абстрактный метод "периметр фигуры"
        pass


class Circle(Shape):  # Класс "Круг"
    def __init__(self, radius):  # Конструктор класса
        self.radius = radius

    def area(self):  # Переопределение метода
        return math.pi * (self.radius ** 2)

    def perimeter(self):  # Переопределение метода
        return 2 * math.pi * self.radius

    def __str__(self):  # Как показывать при печати
        return f"Круг с радиусом {self.radius}"


class Rectangle(Shape):  # Класс "Прямоугольник"
    def __init__(self, width, height):  # Конструктор класса
        self.width = width
        self.height = height

    def area(self):  # Переопределение метода
        return self.width * self.height

    def perimeter(self):  # Переопределение метода
        return 2 * (self.width + self.height)

    def __str__(self):  # Как показывать при печати
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"


# Класс для представления треугольника
class Triangle(Shape):
    def __init__(self, a, b, c):  # Конструктор класса
        self.a = a
        self.b = b
        self.c = c

    def area(self):  # Переопределение метода
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):  # Переопределение метода
        return self.a + self.b + self.c

    def __str__(self):  # Как показывать при печати
        return f"Треугольник со сторонами {self.a}, {self.b} и {self.c}"


def test_shapes():
    # Создание объекта класса "Круг"
    circle = Circle(5)
    assert str(circle) == "Круг с радиусом 5"
    assert abs(circle.area() - 78.53) < 0.01
    assert abs(circle.perimeter() - 31.42) < 0.01
    # Создание объекта класса "Прямоугольник"
    rectangle = Rectangle(4, 6)
    assert str(rectangle) == "Прямоугольник с шириной 4 и высотой 6"
    assert rectangle.area() == 24
    assert abs(rectangle.perimeter() - 20) < 0.01
    # Создание объекта класса "Треугольник"
    triangle = Triangle(4, 5, 3)
    assert triangle.area() == 6.0
    assert triangle.perimeter() == 12
    assert str(triangle) == "Треугольник со сторонами 4, 5 и 3"
    print(f"Площадь круга: {circle.area()}")
    print(f"Периметр круга: {circle.perimeter()}")
    print(f"Площадь прямоугольника: {rectangle.area()}")
    print(f"Периметр прямоугольника: {rectangle.perimeter()}")
    print(f"Площадь треугольника: {triangle.area()}")
    print(f"Периметр треугольника: {triangle.perimeter()}")


# == Пример композиции ==
class Engine:  # Двигатель
    def start(self):
        print("Двигатель запущен")

    def stop(self):
        print("Двигатель остановлен")


class Wheels:  # Колеса
    def turn(self, direction):
        print(f"Колеса поворачивают {direction}")


class Car:  # Машина
    def __init__(self):
        self.engine = Engine()  # Композиция
        self.wheels = Wheels()  # Композиция

    def start(self):
        self.engine.start()  # Делегирование
        self.wheels.turn("вперед")  # Делегирование

    def stop(self):
        self.wheels.turn("стоят")  # Делегирование
        self.engine.stop()  # Делегирование


def test_car():
    my_car = Car()
    my_car.start()
    my_car.stop()


class Bag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def __str__(self):
        return ", ".join(self.items)


def test_bag():
    my_bag = Bag()
    my_bag.add("яблоко")
    assert str(my_bag) == "яблоко"
    my_bag.add("банан")
    assert str(my_bag) == "яблоко, банан"
    my_bag.remove("яблоко")
    assert str(my_bag) == "банан"
    my_bag.remove("банан")
    assert str(my_bag) == ""


# Примеры перегрузки операторов:
# Перегрузка +:
class Vector:  # Вектор в двумерном пространстве
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Сложение векторов
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # Вычитание векторов
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


def test_vector():
    v1 = Vector(2, 3)
    v2 = Vector(1, 1)
    assert str(v1 + v2) == "(3, 4)"
    assert str(v1 - v2) == "(1, 2)"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Перегрузка ==
    # Сравнить два объекта на равенство
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


def test_book():
    book1 = Book("1984", "George Orwell")
    book2 = Book("1984", "George Orwell")
    assert book1 == book2
    book3 = Book("Война и мир", "Лев Толстой")
    assert book1 != book3


# Перегрузка [] (операторы индексирования)
class CustomList:
    def __init__(self):
        self.data = {}

    def __getitem__(self, index):
        return self.data.get(index, "No data")

    def __setitem__(self, index, value):
        self.data[index] = value


def test_custom_list():
    my_list = CustomList()
    my_list[5] = "Five"
    assert my_list[5] == "Five"
    assert my_list[2] == "No data"


# Представим, что у нас есть страница авторизации.
# Эта страница содержит поля для ввода имени пользователя и пароля,
# а также кнопку входа в систему.
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.saucedemo.com/")
        self.username_input = (By.XPATH, '//input[@data-test="username"]')
        self.password_input = (By.XPATH, '//input[@data-test="password"]')
        self.login_button = (By.XPATH, '//input[@data-test="login-button"]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


def test_login():
    # Инициализация драйвера Selenium для Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    driver = webdriver.Chrome(options=options)
    # Создание объекта Page Object
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Проверка, что авторизация прошла успешно
    # time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()
