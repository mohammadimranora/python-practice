"""
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""
result = 0
number = int(input("Please enter a value: "))
if number < 17:
    globals()['result'] = 17 - number
else:
    globals()['result'] = (number - 17) * 2

print("Result: ", globals()['result'])
