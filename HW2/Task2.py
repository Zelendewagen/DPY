# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

a = '1/2'
b = '5/8'


def roundup(fraction):
    if fraction[0] % fraction[1] == 0:
        return fraction[0] // fraction[1]
    if fraction[1] % fraction[0] == 0:
        fraction[1] //= fraction[0]
        fraction[0] = 1
    while fraction[0] % 5 == 0 and fraction[1] % 5 == 0:
        fraction[0] //= 5
        fraction[1] //= 5
    while fraction[0] % 3 == 0 and fraction[1] % 3 == 0:
        fraction[0] //= 3
        fraction[1] //= 3
    while fraction[0] % 2 == 0 and fraction[1] % 2 == 0:
        fraction[0] //= 2
        fraction[1] //= 2
    return fraction


def task2(a, b):
    first = list(map(int, a.split('/')))
    second = list(map(int, b.split('/')))

    mult = roundup([first[0] * second[0], first[1] * second[1]])
    if isinstance(mult, list):
        mult = f'{mult[0]}/{mult[1]}'
    checkmult = fractions.Fraction(first[0], first[1]) * fractions.Fraction(second[0], second[1])

    if first[1] % second[1] == 0:
        denominator = first[1] // second[1]
        second = list(map(lambda n: n * denominator, second))
    elif second[1] % first[1] == 0:
        denominator = second[1] // first[1]
        first = list(map(lambda x: x * denominator, first))
    else:
        denominator1 = first[1]
        denominator2 = second[1]
        second = list(map(lambda n: n * denominator1, second))
        first = list(map(lambda x: x * denominator2, first))

    summ = roundup([first[0] + second[0], first[1]])
    if isinstance(summ, list):
        summ = f'{summ[0]}/{summ[1]}'
    checksumm = fractions.Fraction(first[0], first[1]) + fractions.Fraction(second[0], second[1])

    print(f"Сумма: {summ}\n"
          f"Проверка суммы: {checksumm}\n\n"
          f"Произведение: {mult}\n"
          f"Проверка произведения: {checkmult}")


task2(a, b)
