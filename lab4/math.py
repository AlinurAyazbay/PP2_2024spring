#ex1
import math
def degrees_to_radians(degrees):
    radians = degrees * math.pi / 180
    return radians
degrees = float(input())
radians = degrees_to_radians(degrees)
print(radians)

#ex2
def trapezoid_area(h, b1, b2):
    area = (b1 + b2) * h / 2
    return area
h = float(input())
b1 = float(input())
b2 = float(input())
area = trapezoid_area(h, b1, b2)
print(area)

#ex3
import math
def polygon_area(n, s):
    a = (n * s**2) / (4 * math.tan(math.pi / n))
    return a
sides = int(input())
length = float(input())
a = polygon_area(sides, length)
print(a)

#ex4
def area(base, height):
    area = base * height
    return area
length = float(input())
h = float(input())
area = area(length, h)
print(area)
