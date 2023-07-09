# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок
import random
from Chess import Checker


def pacifists_queens_generator():
    rows = (1, 2, 3, 4, 5, 6, 7, 8)
    columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    coordinates = {'queen 1': str(columns[random.randint(0, 7)]) + str(rows[random.randint(0, 7)])}
    beaten_fields = Checker.find_beaten_fields(coordinates['queen 1'])
    for i in range(2, 9):
        check = True
        while check:
            temp = str(columns[random.randint(0, 7)]) + str(rows[random.randint(0, 7)])
            if temp not in beaten_fields:
                coordinates['queen ' + str(i)] = temp
                beaten_fields += Checker.find_beaten_fields(temp)
                beaten_fields = list(set(beaten_fields))
                check = False
                print(coordinates)


pacifists_queens_generator()
