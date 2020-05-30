"""
Write a Python program that will accept the base and height of a triangle and compute the area.
"""


def calculate_area(base, height):
    if base is not None and height is not None:
        return (base * height)/2
    else:
        return None


b, h = map(int, input("Please enter base and height of triangle: ").split())
res = calculate_area(b, h)
print("Area of triangle is {}".format(res))
