"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""


def calculateData(x: int, y: int) -> int:
    return (x + y) * (x + y)


try:
    a, b = map(int, input("Please enter the value of x, y:").split())
    res = calculateData(a, b)
    print(res)
except ValueError as e:
    print("Please enter correct value {}".format(e.__cause__))
except TypeError as e:
    print("Please enter correct value {}".format(e.__cause__))
finally:
    print("Done!")
