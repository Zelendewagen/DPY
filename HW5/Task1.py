# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def task1(path: str):
    *path, name, ext = path.replace('.', '\\').split('\\')
    return '\\'.join(path), name, ext


print(task1(r"C:\Пользователи\Админ\Folder\python.exe"))
