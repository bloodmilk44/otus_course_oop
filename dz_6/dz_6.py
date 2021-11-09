import math


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles


class Triangle(Figure):
    angles = 3
    name = 'Triangle'

    def __init__(self, a, b, c, name, angles):
        super().__init__(name, angles)
        self.a = a
        self.b = b
        self.c = c

    def print_name(self):
        print(Triangle.name)

    def print_angles(self):
        print(Triangle.angles)

    def print_area(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        if a <= 0:
            print('Сторона треугольника не может быть меньше или равна нулю')
        elif b <= 0:
            print('Сторона треугольника не может быть меньше или равна нулю')
        elif c <= 0:
            print('Сторона треугольника не может быть меньше или равна нулю')
        else:
            p = (a + b + c / 2)
            s = round(math.sqrt(p), 2)
            print(s)


class Rectangle(Figure):
    angles = 4
    name = 'Rectangle'


class Square(Figure):
    angles = 4
    name = 'Square'


class Circle(Figure):
    angles = 0
    name = 'Circle'


triangle_2 = Triangle(6, 5, 20, name=Triangle, angles=3)
triangle_2.print_area()
triangle_2.print_name()
triangle_2.print_angles()