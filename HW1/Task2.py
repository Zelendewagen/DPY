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


def task2():
    # Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
    # Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
    # Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

    number = Checkint("")
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count == 0:
        print("Число простое")
    else:
        print("Чиcло составное")


task2()
