# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
from shutil import copyfile
import sys


def make_dir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        return False
    else:
        return True


def del_dir(dir):
    try:
        os.rmdir(dir)
    except OSError:
        return False
    else:
        return True

def show_dir(path):
    list_dir = []
    for dir in os.listdir(path):
        if os.path.isdir(dir):
            list_dir.append(dir)
    return list_dir

def show_files(path):
    list_dir = []
    for dir in os.listdir(path):
        if os.path.isfile(dir):
            list_dir.append(dir)
    return list_dir


if __name__ == '__main__':

    # Задача - 1
    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        if make_dir(dir_name):
            print('Каталог {} успешно создан'.format(dir_name))
        else:
            print('Невозможно создать каталог {}'.format(dir_name))

    for i in range(1, 10):
        dir_name = 'dir_' + str(i)
        if del_dir(dir_name):
            print('Каталог {} успешно удален'.format(dir_name))
        else:
            print('Невозможно удалить каталог {}'.format(dir_name))

    # Задача - 2
    path = os.getcwd()
    print('Папки текущей директории: ' + str(show_dir(path)))

    # Задача - 3
    file_name = sys.argv[0]
    copyfile(file_name, 'Копия_' + file_name)

