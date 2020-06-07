"""
Write a Python program to display your details like name, age, address in three different lines.
"""


def printData(name: str, age: int, address: str) -> bool:
    if name is not None and age > 0 and address is not None:
        print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
    else:
        print("Please enter correct value")


nameOutside = input("Please enter name")
ageOutside = input("\nPlease enter age")
addressOutside = input("\nPlease enter address")

print(nameOutside, ageOutside, addressOutside)