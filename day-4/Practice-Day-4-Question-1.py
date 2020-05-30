"""
Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
"""


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


number = int(input("Please enter a number: "))
res = check_even(number)
if res:
    print("{} is even".format(number))
else:
    print("{} is odd".format(number))
