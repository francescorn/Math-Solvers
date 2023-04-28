from math import sqrt
from math import pi

def sanitize_results(input):
    if input != int or input != float or input < 0:
        print("Please enter a number greater than 0")
        exit(1)
    
    return input

def circle():
    radius = sanitize_results(input("Input the length of the radius: "))

    area = pi * radius * radius
    print(f"The area of the circle is: {area}")

def triangle():
    base = sanitize_results(input("Length of base of triangle: "))
    height = sanitize_results(input("Height of triangle: "))
    
    area = base * height / 2
    print(f"The area of the triangle is: {area}")

    
def square():
    length = sanitize_results(input("Length of square: "))

    area = length * length
    print(f"The area of the square is: {area}")


def rectangle():
    length = sanitize_results(input("Length of rectangle: "))
    height = sanitize_results(input("Height of rectangle: "))

    area = length * height
    print(f"The area of the rectangle is: {area}") 


def trapezoid():
    height = sanitize_results(input("Height of trapezoid: "))
    base_1 = sanitize_results(input("Base one value: "))
    base_2 = sanitize_results(input("Base two value: "))

    area = ((base_1 + base_2) / 2) * height
    print(f"The area of the trapezoid is: {area}")


def rhombus():
    height = sanitize_results(input("Height of rhombus: "))
    base = sanitize_results(input("Base of rhombus: "))
    
    area = height * base
    print(f"The area of the rhombus is: {area}")


def pentagon():
    side = sanitize_results(input("Length of one side of pentagon:"))
    
    area = sqrt(5 * (5 + 2 *(sqrt(5)))) * side * side / 4
    print(f"The area of the regular pentagon is: {area}")


def hexagon():
    side = sanitize_results(input("Length of one side of hexagon:"))
    height = sanitize_results(input("Height of one side of hexagon:"))

    area = ( (6 * side * height) + (3 * sqrt(3) * side * side))
    print(f"The area of the regular hexagon is: {area}")


#Area of a shape:
shape = input("Please enter the name of the shape: ")

if shape.lower() == "circle":
    circle()

elif shape.lower() == "triangle":
    triangle()

elif shape.lower() == "square":
    square()

elif shape.lower() == "rectangle":
    rectangle()

elif shape.lower() == "trapezoid":
    trapezoid()

elif shape.lower() == "rhombus":
    rhombus()

elif shape.lower() == "pentagon":
    pentagon()

elif shape.lower() == "hexagon":
    hexagon()
    
else:
    print("Please enter: circle, triangle, square, rectangle, trapezoid, rhombus, pentagon, or hexagon")