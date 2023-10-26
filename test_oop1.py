# Создание классов и объектов
def test_dog():
    class Собака:  # Класс "Собака"
        def __init__(self, name):  # Конструктор класса
            self.name = name  # У собаки есть имя и оно будет храниться в атрибуте name

        def полаять(self):  # Полаять
            print(f"{self.name} говорит Гав!")

    # Мы создаём объект класса Собака
    моя_собака = Собака("Тузик")
    моя_собака.полаять()
    assert моя_собака.name == "Тузик"
    # Второй объект класса Собака
    вторая_собака = Собака("Шарик")
    вторая_собака.полаять()


# == Инкапсуляция ==
# Использование инкапсуляции для защиты данных
class Circle:  # Класс Круг
    def __init__(self, radius):  # Конструктор класса
        self.radius = radius  # Публичный атрибут

    def perimeter(self):  # Длина окружности
        self._hidden_method()
        self.__private_method()
        return 2 * 3.14 * self.radius  # Публичный метод

    def area(self):  # Публичный метод "площадь круга"
        return 3.14 * self.radius * self.radius  # Публичный метод

    def _hidden_method(self):
        print("Скрытый метод")

    def __private_method(self):
        print("Приватный метод - можно использовать только в этом классе")


def test_circle():
    assert Circle(10).area() == 314.0
    assert Circle(21).area() == 1384.74
    assert abs(Circle(10).perimeter() - 62.8) < 0.001
    c = Circle(10)
    c._hidden_method()
    # c.__private_method()


# Наследование и переопределение методов
# Реализация полиморфизма
class Animal:  # Базовый класс "Животное"
    def __init__(self, name):  # Конструктор класса
        self.name = name  # Публичный атрибут

    def speak(self):
        print("Я не знаю как я говорю!")

    def speak_with_name(self):
        return f"{self.name} говорит: {self.speak()}"


class Dog(Animal):  # Класс "Собака"
    def speak(self):  # Переопределение метода
        return "Гав!"


class Cat(Animal):  # Класс "Кошка"
    def speak(self):  # Переопределение метода
        return "Мяу!"


class Cow(Animal):  # Класс "Корова"
    def speak(self):  # Переопределение метода
        return "Муу!"


class Fish(Animal):  # Класс "Рыба"
    def speak(self):  # Переопределение метода
        return "Буб!"


def animal_sound(animal: Animal):
    print(animal.speak_with_name())


def test_animals():
    assert Dog("Тузик").speak() == "Гав!"
    assert Cat("Пушок").speak() == "Мяу!"
    assert Cow("Бурёнка").speak() == "Муу!"
    assert Fish("Дори").speak() == "Буб!"
    animals = [Dog("Тузик"), Cat("Пушок"), Cow("Бурёнка"),
               Cat("Рыжик"), Fish("Дори")]
    for animal in animals:
        print(animal.speak_with_name())  # Полиморфизм
    for animal in animals:
        animal_sound(animal)


# == Обновление метода ==
# Иногда вы можете захотеть сохранить исходное поведение метода,
# но добавить к нему дополнительную функциональность.
# Это можно сделать с помощью функции super():
class SmallDog(Dog):
    def speak(self):
        print("Будьте осторожны с маленькой собакой!")
        # вызываем исходный метод из родительского класса
        return super().speak() + " ...но это маленькая собака."


def test_small_dog():
    small_dog = SmallDog("Малыш")
    assert small_dog.speak() == "Гав! ...но это маленькая собака."


# == Расширение методов ==
# Добавление новой функциональности к классам
# без изменения исходного кода класса.
# Это можно делать с помощью наследования или миксинов

# Миксин — это класс, который содержит методы для использования в других классах
# Миксин "Вилять хвостом"
class WagTailMixin:
    def __init__(self, name):
        self.name = name

    def wag_tail(self):  # Новый метод "махать хвостом"
        print(f"{self.name} машет хвостом!")


# Класс "Счастливая собака"
class HappyDog(Dog, WagTailMixin):  # Множественное наследование
    pass


def test_happy_dog():
    h_dog = HappyDog("Бобик")
    print(h_dog.speak())
    h_dog.wag_tail()


# Класс "Несчастный кот"
class UnhappyCat(Cat, WagTailMixin):  # Множественное наследование
    pass


def test_unhappy_cat():
    u_cat = UnhappyCat("Рыжик")
    print(u_cat.speak())
    u_cat.wag_tail()


# Пример использования инкапсуляции
class BankAccount:
    # Здесь баланс счёта __balance — приватный атрибут.
    # Он не доступен извне класса напрямую,
    # и чтобы получить его значение,
    # нужно использовать метод get_balance
    def __init__(self, balance=0):
        self.__balance = balance
        self.__transactions = [f"Начальный баланс: {balance}"]

    def deposit(self, amount):  # Внести сумму на счёт
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Пополнили на {amount}")
            return self.__balance
        else:
            print(f"{amount} - некорректная сумма для депозита "
                  f"(должна быть положительной)")

    def withdraw(self, amount):  # Снять сумму со счёта
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Сняли {amount}")
            return self.__balance
        else:
            print(f"{amount} - некорректная сумма для снятия "
                  f"(должна быть положительной и <= баланса)")

    def get_balance(self):  # Получить текущий баланс
        return self.__balance

    def show_transactions(self):  # Показать список транзакций
        for t in self.__transactions:
            print(t)
        print(f"Текущий баланс: {self.__balance}")


def test_bank_account():
    account = BankAccount(1000)
    assert account.get_balance() == 1000
    print(account.deposit(500))
    assert account.get_balance() == 1500
    print(account.deposit(-100))
    assert account.get_balance() == 1500
    assert account.withdraw(200) == 1300
    account.show_transactions()


class Car:  # Класс "Машина"
    def __init__(self):  # Конструктор класса
        self.__update_software()  # Вызов приватного метода

    def drive(self):  # Публичный метод
        print("Машина едет")

    # Метод __update_software приватный и предназначен
    # для внутреннего использования в классе.
    # Может быть полезно, например, чтобы предотвратить
    # вызов этого метода извне или из производных классов
    def __update_software(self):  # Приватный метод
        print("Обновление программного обеспечения")


def test_car():
    car = Car()
    car.drive()
    # car.__update_software()  # Мы не можем так вызвать
