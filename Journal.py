path = "C:/Users/Rossvik/Desktop/journal.txt"
# Выводим учеников из файла, у которых оценка меньше 3
dict_ = {}
with open(path, 'r', encoding='utf8') as file_:
    str_ = file_.readlines()
    for item_ in  str_:
        dict_[item_.rstrip()[0:-1]] = int(item_.rstrip()[-1])
    for key, item in dict_.items():
        if item < 3:
            print(key)
# Реверсирование строк файла (перестановка строк файла в обратном порядке)
with open(path, 'r', encoding='utf8') as file_:
    str_ = file_.readlines()
    str_.reverse()
    with open(path, 'w', encoding='utf8') as file_2:
        file_2.writelines(str_)
