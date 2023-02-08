# Напишите контекстный менеджер, который умеет безопасно работать с файлами.
# В конструктор объекта контекстного менеджера передаются два аргумента:
# первый — путь к файлу, который надо открыть, второй — тип открываемого файла (для записи, для чтения и т. д.).
# При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
# При выходе из контекстного менеджера файл должен закрываться.
# (Эталоном работы можно считать контекстный менеджер open).
from datetime import datetime
from contextlib import contextmanager  # импортируем нужный нам декоратор


@contextmanager  # оборачиваем функцию в декоратор contextmanager
def open_file(path, methods):
    f = open(path, methods, encoding='"utf-16"')
    yield f  # если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
    f.close()


with open_file("C:/Users/Rossvik/Desktop/journal.txt", "a") as file_:
    file_.write("Запись текста через контекстный менеджер")


class OpenFile:
    def __init__(self, path, type_):
        self.file = open(path, type_)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile("C:/Users/Rossvik/Desktop/journal.txt", "a") as f:
    f.write('Мой контекстный менеджер делает то же самое!')
