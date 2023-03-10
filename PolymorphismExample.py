import math
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


# возведение в степень **2 (в квадрат)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Площадь круга: {round(math.pi * self.radius ** 2, 3)}'
