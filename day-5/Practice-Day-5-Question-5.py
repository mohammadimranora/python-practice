"""
Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20
"""


def get_result(x, y) -> int:
    sums = x + y
    if (sums >= 15) and (sums <= 20):
        sums = 20
        return sums
    else:
        return sums


try:
    a, b = map(int, input("Please enter two values: ").split())
    res = get_result(a, b)
    print(res)
except ValueError as e:
    print("Please enter two numbers")
finally:
    print("Successfully executed, exit 0")

