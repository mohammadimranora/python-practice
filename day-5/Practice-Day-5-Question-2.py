"""
Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

import sys


def lcm(x, y) -> int:
    """
    Function return the lowest common multiple
    :param x:
    :param y:
    """
    value = 0
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            globals()['value'] = greater
            break
        greater += 1
    return globals()['value']


a, b = map(int, input("Please enter tow values: ").split())
res = lcm(a, b)
print(res)
