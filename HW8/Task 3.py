# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий. Соберите из созданных на уроке и в рамках
# домашнего задания функций пакет для работы с файлами разных форматов.
from statistics import mean

from Module import for_another as wwf, for_file as anw
import time

tries = []
for _ in range(10):
    start_time = time.time()
    wwf.generate_dict('D:\\Курсы', './out')
    tries.append(time.time() - start_time)
print("Мой вариант: %s секунд" % (mean(tries)))

tries = []
for _ in range(10):
    start_time = time.time()
    anw.folders_info('D:\\Курсы', './out')
    tries.append(time.time() - start_time)
print("Вариант Анатолия: %s секунд" % (mean(tries)))
