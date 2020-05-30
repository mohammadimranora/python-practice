"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""


def isinthousand(num):
    return (abs(1000 - num) <= 100) or (abs(2000 - num) <= 100)


number = int(input("Please enter a number: "))

result = isinthousand(number)
print(result)