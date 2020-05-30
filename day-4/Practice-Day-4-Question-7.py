"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""


def concatenate_element_string(values):
    output = ''
    for ele in values:
        output += str(ele)
    return output


val = list(map(int, input("Please enter values in the list: ").split()))
res = concatenate_element_string(val)
print(res)
