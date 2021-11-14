import pytest
from dz_6.dz_6 import Triangle, Rectangle, Square, Circle

triangle = Triangle(6, 5, 20, name=Triangle.name, angles=Triangle.angles)
rectangle = Rectangle(6, 6, 7, 7, name=Rectangle.name, angles=Rectangle.angles)
square = Square(6, name=Square.name, angles=Square.angles)
circle = Circle(name=Circle.name, angles=Circle.angles, p=5)


def test_triangle():
    assert triangle.print_name() == Triangle.name
    assert triangle.print_angles() == Triangle.angles
    assert triangle.print_area() == 4.58
    assert triangle.print_angles() == 3

def test_rectangle():
    assert rectangle.print_name() == Rectangle.name
    assert rectangle.print_angles() == Rectangle.angles
    assert rectangle.print_area() == 36
    assert rectangle.print_angles() == 4

def test_square():
    assert square.print_name() == Square.name
    assert square.print_angles() == Square.angles
    assert square.print_area() == 36
    assert square.print_angles() == 4

def test_circle():
    assert circle.print_name() == Circle.name
    assert circle.print_angles() == Circle.angles
    assert circle.print_area() == 19.625
    assert circle.print_angles() == 0