"""
Write a Python program to add two objects if both objects are an integer type.
"""


def addTwoInt(a,b) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b


try:
    a, b = map(int, input("Please enter value of a and b: ").split())
    res = addTwoInt(a, b)
    print(res)
except ValueError:
    print("Please enter integer value")
finally:
    print("Done")