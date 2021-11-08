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

    def triangl_area(self, a, b ,c):
        return self.a + self.b + self.c


class Rectangle(Figure):
    angles = 4
    name = 'Rectangle'


class Square(Figure):
    angles = 4
    name = 'Square'


class Circle(Figure):
    angles = 0
    name = 'Circle'

test = Triangle(10, 3, 4, 4 ,5)
test_2 = Triangle.triangl_area
print(test_2)