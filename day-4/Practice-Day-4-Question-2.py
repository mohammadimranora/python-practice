"""
Write a Python program to count the number 4 in a given list
"""
count = 0


def count_number_four(listuser):
    if len(listuser):
        for val in listuser:
            if val == 4:
                globals()['count'] += 1

    return globals()['count']


# Reading a list
values = list(map(int, input("Please enter value").split()))
res = count_number_four(values)
print(res)