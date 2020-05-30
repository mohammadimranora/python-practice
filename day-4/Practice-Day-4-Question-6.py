"""
Write a Python program to create a histogram from a given list of integers.
"""


def generate_histogram(sym, ints):
    for i in range(len(ints)):
        output = ''
        ran = ints[i]
        for j in range(0, ran):
            output += sym
        print(output)


symbol = input("Please enter symbol for histogram: ")
integers = list(map(int, input("please enter integers for histogram: ").split()))
generate_histogram(symbol, integers)