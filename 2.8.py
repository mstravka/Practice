import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

decorator_name = "@abstractmethod"
print(f"\033[95m{decorator_name}\033[0m")

shapes = [Circle(4), Rectangle(5,3)]
for s in shapes:
    print(f"{type(s).__name__} площа:", s.area())
