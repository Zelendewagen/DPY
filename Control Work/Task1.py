# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
import argparse
from pathlib import Path
import logging
import os

Item = namedtuple("Item", ['name', 'extension', 'directory', 'parent_dir'])
parser = argparse.ArgumentParser()
parser.add_argument('path', help='enter path')
args = parser.parse_args()
path = Path(args.path)

logging.basicConfig(filename='logs.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')
logger = logging.getLogger()

result = []
file_list = os.listdir(path)
for item in file_list:
    item_path = path / item
    name = item_path.stem
    suffix = item_path.suffix or 'none'
    directory = item_path.is_dir()
    parent_dir = item_path.parent.stem
    if directory:
        logger.info(f"item name: {name}, suffix: this is directory, parent_dir: {parent_dir}")
    else:
        logger.info(f"item name: {name}, suffix: {suffix} parent_dir: {parent_dir}")
    result.append(Item(name, suffix, directory, parent_dir))

print(*result, sep='\n')

r"""
Для запуска из терминала:
python .\Task1.py C:\Users
"""
