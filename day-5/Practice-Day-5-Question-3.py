"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""


def get_sum(x, y, z) -> int:
    sum_value = x + y + z
    if x == y:
        sum_value = 0
        return sum_value
    else:
        return sum_value


try:
    a, b, c = map(int, input("Please enter three numbers: ").split())
except ValueError as e:
    print("Please enter numbers")
res = get_sum(a, b, c)
print(res)
