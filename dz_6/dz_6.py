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
        print("Название фигуры: " + Triangle.name)

    def print_angles(self):
        print("Количество углов фигуры: " + str(Triangle.angles))

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

    def print_perimeter(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        p = a + b + c
        print(p)


class Rectangle(Figure):
    angles = 4
    name = 'Rectangle'

    def __init__(self, a, b, c, d, name, angles):
        super().__init__(name, angles)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def print_area(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        d = int(self.d)
        if a == c:
            print("У прямоугольника сторона 'a' и сторона 'c' не должны быть равны" )
        elif b == d:
            print("У прямоугольника сторона 'b' и сторона 'd' не должны быть равны")
        elif a == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        elif b == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        elif c == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        elif d == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        else:
            s = a * b
            print(s)

    def print_name(self):
        print(Rectangle.name)

    def print_angles(self):
        print(Rectangle.angles)


class Square(Figure):
    angles = 4
    name = 'Square'

    def print_name(self):
        print(Square.name)

    def print_angles(self):
        print(Square.angles)


class Circle(Figure):
    angles = 0
    name = 'Circle'

    def print_name(self):
        print(Circle.name)

    def print_angles(self):
        print(Circle.angles)


triangle = Triangle(6, 5, 20, name=Triangle.name, angles=Triangle.angles)
rectangle = Rectangle(6, 6, 7, 7, name=Rectangle.name, angles=Rectangle.angles)
square = Square(name=Square.name, angles=Square.angles)
circle = Circle(name=Circle.name, angles=Circle.angles)


print(triangle.print_name(), triangle.print_angles())
#print(rectangle.print_name(), rectangle.print_angles(), rectangle.print_area())
#print(square.angles, square.name)
#print(circle.angles, circle.name)