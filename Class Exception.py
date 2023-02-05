class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указана сторона квадрата')
        else:
            self.a = a

    def __str__(self):
        return f"Ваше число это {self.a}"


try:
    A = Square(int(input("Введите число: ")))
    print(A)
except NonPositiveDigitException as e:
    print(e)
