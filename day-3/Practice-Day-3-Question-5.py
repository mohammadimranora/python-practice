"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""


def get_larger_string(length, string):
    length = abs(length)
    result = ''
    for i in range(length):
        result = result + string
    return result


value = input("Please enter a string: ")
copies = int(input("Please enter number of copy: "))
res = get_larger_string(copies, value)
print("Result: ", res)