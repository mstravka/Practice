def greet(name):
    return f"Привіт, {name}!"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

print(greet("Марина"))

rect = Rectangle(5, 3)
circle = Circle(4)

print("Площа прямокутника:", rect.area())
print("Площа кола:", circle.area())

r2 = Rectangle(10, 2)
c2 = Circle(7)

print("Площа другого прямокутника:", r2.area())
print("Площа другого кола:", c2.area())
