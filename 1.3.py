import math

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

d = y**2 - 4*x*z

if d > 0:
    r1 = (-y + math.sqrt(d)) / (2*x)
    r2 = (-y - math.sqrt(d)) / (2*x)
    print("Roots:", r1, r2)
elif d == 0:
    r = -y / (2*x)
    print("One root:", r)
else:
    print("No real roots")
