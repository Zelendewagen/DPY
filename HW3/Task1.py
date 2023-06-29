# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

data = {
    'Петя': ('Палатка', 'Спальник', 'Фонарик', 'Газовая горелка',),
    'Иван': ("Палатка", "Спальник", "Тент", "Перчатки"),
    'Игорь': ("Телефон", "Спальник", "Перчатки", "Собака"),
    "Кристина": ("Палатка", "Фонарик", "Кружка")
}

all_unic_items = set()
for i in data:
    all_unic_items = all_unic_items.union(data[i])
print(f'Все три друга взяли: {all_unic_items}')

unique_items = {}
for i in data:
    temp = set(data[i])
    for j in data:
        if i != j:
            temp -= set(data[j])
    unique_items[i] = temp
print(f'Уникальные вещи взяли:{unique_items}')

default_items = {}
for i in data:
    temp = set()
    for j in data:
        if i != j:
            if len(temp) == 0:
                temp = temp.union(set(data[j]))
            else:
                temp.intersection_update(set(data[j]))
    default_items[i] = temp.difference(set(data[i]))
print(f'Вещи которые есть у всех кроме:{default_items}')
