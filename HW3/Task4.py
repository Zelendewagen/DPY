# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
from itertools import combinations

items = {
    "Палатка": 10,
    "Спальник": 1,
    "Инструменты": 3,
    "Огниво": 0.05,
    "Телефон": 0.5,
    "Лодка": 10,
    "Еда": 15,
}

result = []
mw = 15

for i in range(len(items)):
    comb = combinations(items, i)
    for combination in comb:
        temp = items.copy()
        weight = 0
        for item in combination:
            weight += items[item]
            temp.pop(item)
        if weight <= mw:
            lowitem = min(temp.items(), key=lambda item: item[1])
            if weight + lowitem[1] <= mw:
                continue
            else:
                result.append(list(combination) + [weight])
for comb in result:
    print(comb)