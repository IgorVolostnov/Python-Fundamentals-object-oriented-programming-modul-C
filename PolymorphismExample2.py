from PolymorphismExample import Rectangle, Square, Circle

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
rect_3 = Rectangle(12, 5)

# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())
print(rect_3.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

circle_1 = Circle(5)
circle_2 = Circle(10)
circle_3 = Circle(10)

print(circle_1)
print(circle_2)
print(circle_3)

figures = [rect_1, rect_2, rect_3, square_1, square_2, circle_1, circle_2, circle_3]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure)

if rect_2 == rect_3:
    print("Прямоугольники равны")

if circle_2 == circle_3:
    print("Круги равны")
else:
    print("Нет метода сравнения")