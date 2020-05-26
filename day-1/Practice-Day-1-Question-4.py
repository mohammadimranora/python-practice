"""
Write a Python program which accepts the radius of a circle from the user and compute the area
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math
radius = int(input("Please enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
print("r: ", radius)
print("Area: ", area)
