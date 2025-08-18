import math

def circumference(radius):
    return 2 * math.pi * radius

r = float(input("Enter the radius of the circle: "))
print("Circumference of the circle is:", circumference(r))