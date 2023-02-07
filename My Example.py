import os
import math

path = "C:/Users/Rossvik/Desktop/input.txt"
path2 = "C:/Users/Rossvik/Desktop/output.txt"
data_ = ["какие-то данные\n", "ещё какие-то данные\n", "конец данных\n"]
# Выбрать из файла строки с числами и найти наименьшее т наибольшее из них, результат записать в новый файл
list_ = []
while True:
    with open(path, 'r', encoding='utf8') as file_:
        for str_ in file_:
            try:
                list_.append(int(str_))
            except ValueError as e:
                continue
        tuple_ = min(list_), max(list_)
        with open(path2, 'a', encoding='utf8') as file_2:
            file_2.write(str(tuple_[0]) + "\n")
            file_2.write(str(tuple_[1]) + "\n")
        break
