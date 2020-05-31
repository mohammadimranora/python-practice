"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

from math import gcd
a, b = map(int, input("Please enter tow values: ").split())
result = gcd(a, b)
print(result)