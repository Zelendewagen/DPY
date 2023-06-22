# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

a = '324234/2345'
b = '324/2342'


def nod(a, b):
    while b:
        a, b = b, a % b
    return a


def roundup(fraction):
    if fraction[0] % fraction[1] == 0:
        return fraction[0] // fraction[1]
    else:
        fraction[0] //= nod(fraction[0], fraction[1])
        fraction[1] //= nod(fraction[0], fraction[1])
        return fraction


def task2(a, b):
    first = list(map(int, a.split('/')))
    second = list(map(int, b.split('/')))

    mult = [first[0] * second[0], first[1] * second[1]]
    roundup(mult)
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
