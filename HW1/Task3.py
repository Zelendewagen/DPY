from random import randint


def Checkint(name):
    temp = 0
    while temp != 1:
        n = input(f"введите число {name} - ")
        try:
            count = int(n)
            if count < 0 or count > 100000:
                print("Введите число от 0 до 100 тысяч")
            else:
                temp = 1
        except ValueError:
            print("Введено не число!")
    return count


def task3():
    # Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
    # Программа должна подсказывать «больше» или «меньше» после каждой попытки.
    # Для генерации случайного числа используйте код:

    num = randint(0, 1000)
    check = 10
    print(num)
    while check > 0:
        if check == 1:
            count = Checkint(f"(осталось {check} попытка)")
        elif check < 5:
            count = Checkint(f"(осталось {check} попытки)")
        else:
            count = Checkint(f"(осталось {check} попыток)")
        if count < num:
            print("Больше")
        elif count > num:
            print("Меньше")
        else:
            print("Угадал !")
            exit()
        check -= 1
    print("Проиграл :(")


task3()
