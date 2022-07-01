from math import pi


class Rectangle:

    def __init__(self, sideA=0, sideB=0):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return round(pi * (self.radius ** 2))

    def getPerimeter(self):
        return round((2 * pi) * self.radius)


circy = Circle(11)
print(circy.getArea())

circy2 = Circle(4.44)
print(circy2.getPerimeter())