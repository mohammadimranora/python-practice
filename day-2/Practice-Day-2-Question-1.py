"""
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
"""

values = input("Please enter values comma separated")
userList = values.split(",")
userTuple = tuple(userList)

print("List : ", userList)
print("Tuple : ", userTuple)