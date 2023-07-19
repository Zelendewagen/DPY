# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import random


def csv_generator():
    with open("data.csv", 'a', newline='', encoding='utf-8') as f:
        csv_file = csv.writer(f)
        for i in range(100, random.randint(101, 1000)):
            csv_file.writerow([random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)])


def dec_csv(func):
    def wrapper(*args, **kwargs):
        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i in reader:
                result = func(*map(int, i))
        return result

    return wrapper


def dec_json(func):
    res_list = []

    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {
            'args': args,
            'kwargs': kwargs,
            'result': func_res
        }
        res_list.append(result)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(res_list, f)
        return func_res

    return wrapper


@dec_csv
@dec_json
def square_equation_roots(a: int = 0, b: int = 0, c: int = 0):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 0
    elif d == 0:
        if a:
            x1 = x2 = -b / (2 * a)
        else:
            return 0
    else:
        if a:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
        else:
            return 0
    return x1, x2


square_equation_roots()
