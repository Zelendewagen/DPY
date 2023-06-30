# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем,используйте его строковое представление.

def task2(**kwargs):
    result = {}
    for value, key in kwargs.items():
        if key.__hash__:
            result[key] = value
        else:
            result[key.__str__()] = value
    print(result)


task2(one=1, two=2, five=['5'])
