# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def task3(count):
    a, b = 0, 1
    while count != 0:
        sum = a + b
        a,b = b,sum
        count -= 1
        yield sum


for i in task3(7):
    print(i)
