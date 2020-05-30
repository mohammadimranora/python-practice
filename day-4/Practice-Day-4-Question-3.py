"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2
"""


def copies_n_occur(string, copies):
    result = ''
    part = string[0:2]
    for i in range(copies):
        result = result + part
    return result


st = input("Please enter the string: ")
copy = int(input("please enter the number of copies: "))
res = copies_n_occur(st, copy)
print(res)