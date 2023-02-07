import os

os.getcwd()  # какой путь в данный момент используется
os.name  # вы получите информацию о том, с какой платформой вы работаете
os.environ  # полезная информация, такая как количество процессоров, тип ОЗУ, имя компьютера, и т.д.
os.chdir(r'C:\Users\Rossvik\Desktop')  # смена директории
os.chdir("..")  # подняться на один уровень выше
os.listdir()  # с помощью функции os.listdir() можно получить весь список файлов, находящихся в директории
os.mkdir("test")  # создание папки
path = r'C:\Users\Rossvik\Desktop\pytest'  # создание папки через переменную
os.mkdir(path)
path = r'C:\Users\Rossvik\Desktop\pytest\2023\02\07'  # создает промежуточные папки в пути, если их там нет
os.makedirs(path)
os.removedirs("pytest")  # удаляет пустой каталог
os.rename("test.txt", "pytest.txt")  # применяется тогда, когда нужно переименовать файл или папку
os.startfile(r'C:\Users\Rossvik\Desktop\Аналитика по количеству пользователей.jpg')  # позволяет нам
# «запустить» файл в привязанной к нему программе
path = r'C:\Users\Rossvik\Desktop\JS'

for root, dirs, files in os.walk(path):  # получить доступ ко всем её подкаталогам и файлам
    print(root)
    for _dir in dirs:
        print(_dir)

    for _file in files:
        print(_file)
os.path

os.path.basename  # Функция basename вернет название файла пути
os.path.dirname  # Функция dirname возвращает только часть каталога пути
os.path.exists  # Функция exists говорит нам, существует ли файл, или нет
os.path.isdir and os.path.isfile  # Методы isdir и isfile тесно связаны с методом exists,
# так как они также тестируют присутствие или отсутствие файлов, или папок на тех или иных путях
os.path.join  # Метод join позволяет вам совместить несколько путей при помощи присвоенного разделителя
os.path.split  # Метод split разъединяет путь на кортеж, который содержит и файл и каталог
