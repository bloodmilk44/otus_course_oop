import math


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    def print_name(self):
        return ("\nНазвание фигуры: " + self.name)

    def print_angles(self):
        return ("\nКоличество углов фигуры: " + str(self.angles))

class Triangle(Figure):
    angles = 3
    name = 'Triangle'

    def __init__(self, a, b, c, name, angles):
        super().__init__(name, angles)
        self.a = a
        self.b = b
        self.c = c


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
            return ("\nПлощадь фигуры: " + str(s))

    def print_perimeter(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        p = a + b + c
        if a <= 0:
            print('Сторона треугольника не может быть меньше или равна нулю')
        elif b <= 0:
            print('Сторона треугольника не может быть меньше или равна нулю')
        elif c <= 0:
            return ('\nСторона треугольника не может быть меньше или равна нулю')
        else:
            return ("\nПериметр фигуры: " + str(p))


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
            return ("\nСторона прямоугольника не может быть равна нулю")
        else:
            s = a * b
            return ("\nПлощадь фигуры: " + str(s))

    def sum_of_sides(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        d = int(self.d)
        if a == c:
            print("У прямоугольника сторона 'a' и сторона 'c' не должны быть равны")
        elif b == d:
            print("У прямоугольника сторона 'b' и сторона 'd' не должны быть равны")
        elif a == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        elif b == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        elif c == 0:
            print("Сторона прямоугольника не может быть равна нулю")
        elif d == 0:
            return ("\nСторона прямоугольника не может быть равна нулю")
        else:
            p = a + b + c + d
            return ("\nПериметр фигуры: " + str(p))


class Square(Figure):
    angles = 4
    name = 'Квадрат'

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
        if a == b == c == d:
            s = a * b
            return ("\nПлощадь фигуры: " + str(s))
        else:
            return ("\nВсе стороны квадрата должны быть равны")

    def sum_of_sides(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        d = int(self.d)
        if a == b == c == d:
            p = a + b + c + d
            return ("\nПериметр фигуры: " + str(p))
        else:
            return ("\nВсе стороны квадрата должны быть равны")



class Circle(Figure):
    angles = 0
    name = 'Circle'

    def __init__(self, p, name, angles):
        super().__init__(name, angles)
        self.p = p

    def print_area(self):
        p_digit = 3.14
        p = int(self.p)
        if p > 0:
            s = p_digit * (p ** 2) / 4
            return ("\nПлощадь фигуры: " + str(s))
        else:
            return ("Периметр не может быть равен нулю")

    def print_circumference(self):
        p_digit = 3.14
        p = int(self.p)
        if p > 0:
            s = round(p_digit * p)
            return ("\nДлина окружности: " + str(s))
        else:
            return ("\nПериметр не может быть равен нулю")



triangle = Triangle(6, 5, 20, name=Triangle.name, angles=Triangle.angles)
rectangle = Rectangle(6, 6, 7, 7, name=Rectangle.name, angles=Rectangle.angles)
square = Square(6, 6, 6, 6, name = Square.name, angles = Square.angles)
circle = Circle(name=Circle.name, angles=Circle.angles, p = 5)


print(circle.print_name())
print(circle.print_angles())
print(rectangle.print_angles())