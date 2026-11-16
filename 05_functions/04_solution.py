import math
radius = int(input("Enter the radius of the circle : "))
def Circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius 

    return area, circumference

a, c = Circle(radius)

print("Area: ",a, "\nCircumference: ", c)