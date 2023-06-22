# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def task1():
    lst = ('a', 'b', 'c', 'd', 'e', 'f')
    temp = 0
    while temp != 1:
        n = input(f"введите число: ")
        try:
            count = int(n)
            temp = 1
        except ValueError:
            print("Введено не число!")
    print(hex(count))  # проверка результата
    result = []
    while count > 0:
        temp = divmod(count, 16)
        if 9 < temp[1] < 16:
            result.insert(0, str(lst[temp[1] % 10]))
        else:
            result.insert(0, str(temp[1]))
        count = temp[0]

    return '0x' + ''.join(result)


print(task1())

# print(19 % 16, (19 // 16) % 16)#
# print(divmod(16, 16)[1])
