# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
class CheckName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        """Метод, проверяющий, что имя состоит только из букв и начинается на заглавную"""
        if not value.istitle() or not value.isalpha():
            raise ValueError(f'Неверное значение {value}.\n'
                             f'ФИО должно состоять только из букв и начинаться на заглавную')


class CheckSubject:
    def __init__(self, path):
        self.path = path

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что предмет находится в списке"""
        with open(self.path, 'r', newline='', encoding='utf-8') as c:
            if value not in [sub.strip() for sub in c]:
                raise ValueError(f'Предмета {value} нет в списке')


class CheckScoreRange:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что оценки входят в диапазон"""
        if 2 >= value or value > 5:
            raise ValueError(f"Некорректная оценка: {value}\n"
                             f"Оценка должна быть в диапазоне от 2 до 5")


class CheckTestScoreRange:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что результаты тестов входят в диапазон"""
        if 0 >= value or value > 100:
            raise ValueError(f"Некорректная результат теста: {value}\n"
                             f"Результат должен быть в диапазоне от 0 до 100")
