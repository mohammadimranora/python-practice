"""
Write a Python program to test whether a passed letter is a vowel or not.
"""


def check_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    index = vowels.index(character)
    if index >= 0:
        return True
    else:
        return False


value = input("Please enter a character: ")[:1]
res = check_vowel(value)
if res:
    print("{} is vowel".format(value))
else:
    print("{} is consonant".format(value))

