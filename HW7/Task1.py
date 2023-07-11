# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

from pathlib import Path


def group_rename(new_name, ext, new_ext):
    files = [i for i in Path.cwd().iterdir() if i.suffix[1:] == ext]
    for pos, file in enumerate(files, start=1):
        file.rename(f"{file.stem}_{new_name}_{pos}.{new_ext}")


group_rename('copy', 'bat', 'txt')

