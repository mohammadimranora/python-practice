"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
"""

import  math


def distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))


print(distance(4, 0, 6, 6))
print(distance(4, 5, 5, 6))
print(distance(4, 7, 6, 5))