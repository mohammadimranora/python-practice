"""
Write a Python program that will return true if the two given integer values
are equal or their sum or difference is 5
"""


def get_result(x, y) -> bool:
    """
    Return the expected result
    :param x:
    :param y:
    :return:
    """
    sums = x - y
    subs = x - y
    if x == y or sums == 5 or subs == 5:
        return True
    else:
        return False


try:
    a, b = map(int, input("please enter two numbers").split())
    res = get_result(a, b)
    print(res)
except ValueError as e:
    print("Please enter a number")
finally:
    print("Successfully executed and computed the result")
