# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random


def find_beaten_fields(coordinate):
    result = []
    columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    column = columns.index(coordinate[0])
    for i in range(1, 9):
        result.append(coordinate[0] + str(i))
        if columns[i - 1] + coordinate[1] not in result:
            result.append(columns[i - 1] + coordinate[1])
        if 0 <= column - i < 8:
            if int(coordinate[1]) + i < 9:
                result.append(columns[column - i] + str(int(coordinate[1]) + i))
            if int(coordinate[1]) - i > 0:
                result.append(columns[column - i] + str(int(coordinate[1]) - i))
        if 0 <= column + i < 8:
            if int(coordinate[1]) + i < 9:
                result.append(columns[column + i] + str(int(coordinate[1]) + i))
            if int(coordinate[1]) - i > 0:
                result.append(columns[column + i] + str(int(coordinate[1]) - i))

    return result
