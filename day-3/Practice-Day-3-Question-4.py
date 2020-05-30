"""
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
"""


def check(string):
    if string.find("Is") != -1:
        return string
    else:
        return "Is" + string


value = input("Please enter the string to check: ")
result = check(value)
print(result)