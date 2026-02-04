def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    import math
    return math.pi * radius ** 2

print("Процедурний підхід:")
print("Площа прямокутника 5x3:", rectangle_area(5, 3))
print("Площа кола радіусом 4:", circle_area(4))

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

shapes = [Rectangle(5,3), Circle(4)]
for s in shapes:
    print(f"Площа {s.__class__.__name__}:", s.area())
