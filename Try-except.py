#Создать скрипт, который будет в input() принимать строки, и их необходимо будет конвертировать в числа,
#добавить try-except на то, чтобы строки могли быть сконвертированы в числа.
try:
    Value = input("Введите число: ")
    if isinstance(float(Value), float):
        print("Вы ввели правильное число: ")
except ValueError:
    print("Вы ввели неправильное число")
else:
    print(Value)
finally:
    print("Выход из программы")
