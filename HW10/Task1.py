# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Fabric:
    """Фабрика, принимающая класс и возвращающая новый объект такого-же класса"""

    def __init__(self, obj, *args):
        """
        Конструктор класса.
        :param obj: Ссылка на класс
        :param args: Аргументы необходимые для создания нового класса
        """
        self.obj_class = obj
        self.obj_attrs = args

    def do_copy(self):
        """Метод возвращающий новый объект класса на основе входных данных"""
        return self.obj_class(*self.obj_attrs)


class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class Fish(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Мелководная", "Глубоководная")[self.feature > 1000]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nГлубина: {self.feature}\nТип: {self.type}\n'


class Bird(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Небольшой размах", "Большой размах")[self.feature > 3]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nРазмах крыльев: {self.feature}\nТип: {self.type}\n'


class Mammals(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Мелкий", "Крупный")[self.feature > 100]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВес: {self.feature}\nТип: {self.type}\n'


fish = Fish('Nemo', 3, 500)
new_fish = Fabric(Fish, 'Nemo1', 3, 500).do_copy()
print(new_fish)
