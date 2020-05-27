"""
Write a Python program to accept a filename from the user and print the extension of that.
"""

fileName = input("Please enter file name")
fNameExtension = fileName.split(".")
print("File Extension: ", fNameExtension[-1])
