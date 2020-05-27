"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
from math import pow
import sys
value = int(input("Please enter a value"))
result = int("%s" % value) + int("%s%s" % (value, value)) + int("%s%s%s" % (value, value, value))
print(result)
