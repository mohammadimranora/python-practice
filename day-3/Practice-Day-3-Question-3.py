"""
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum.
"""


def value(x, y, z):
    res = x + y + z
    if x == y == z:
        return res * 3
    else:
        return res


a, b, c = input("Please enter value of a,b,c: ").split()
result = value(int(a), int(b), int(c))
print(result)