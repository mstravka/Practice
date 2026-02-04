import math

v = float(input())
angle = float(input())

g = 9.8
angle_rad = math.radians(angle)

time = (2 * v * math.sin(angle_rad)) / g
distance = (v**2 * math.sin(2 * angle_rad)) / g

print(time)
print(distance)

t = 0
step = 0.5

while t <= time:
    x = v * math.cos(angle_rad) * t
    y = v * math.sin(angle_rad) * t - (g * t**2) / 2
    print(x, y)
    t += step
