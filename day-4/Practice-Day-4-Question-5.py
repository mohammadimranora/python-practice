"""
Write a Python program to check whether a specified value is contained in a group of values.
"""
group = [1, 3, 5, 6, 7, 8, 9, 7]


def check_value_for_group(value, group):
    try:
        index = group.index(value)
    except ValueError as e:
        return False
    if index >= 0:
        return True
    else:
        return False


val = int(input("Please enter a value: "))
res = check_value_for_group(val, globals()['group'])
if res:
    print("In the group,{}->{}".format(val, globals()['group']))
else:
    print("Not in the group")
