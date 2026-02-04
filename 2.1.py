import math

def triangle_area(base, height):
    return 0.5 * base * height

def square_area(side):
    return side ** 2

print("Процедурний підхід:")
print("Площа трикутника 6x4:", triangle_area(6, 4))
print("Площа квадрата зі стороною 5:", square_area(5))
