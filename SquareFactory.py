class Square:

    # Устанавливаем свойство класса: сторона квадрата
    @property
    def side_square_property(self):
        return self.side

    # Хотим, чтобы наше свойство: сторона квадрата не была отрицательной
    @side_square_property.setter
    def side_square_property(self, value):
        if value >= 0:
            self.side = value
        else:
            raise ValueError("The side of the square should not be negative")

    # Выводим строку с данными при вызове переменной, которой присвоили объект данного класса
    def __str__(self):
        return f'Квадрат со стороной: {self.side_square_property}'

    # Устанавливаем новое свойство: площадь квадрата
    @property
    def square_area(self):
        return f'Площадь квадрата: {self.side_square_property ** 2}'


class SquareFactory:

    # Устанавливаем статический метод, который создает новый объект класса "Square"
    @staticmethod
    def Object_square(value_side_square):
        S = Square()
        S.side_square_property = value_side_square
        return S


try:
    #Square1 = SquareFactory.Object_square(1.256)
    Square1 = Square()
    Square1.side_square_property = -5
    print(Square1)
    print(Square1.square_area)
except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения)
    print("Ошибки не произошло")
finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
    print("Finally на месте")

print("Код, после блока TRY исключения")


