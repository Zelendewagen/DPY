# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list = [1, 2, 3, '3', 4, 4, 3, 5, 5, 5, 1]
result = []
for i, item in enumerate(list):
    list.remove(item)
    if item in list and item not in result:
        result.append(item)
print(result)
