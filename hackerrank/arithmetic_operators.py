"""
Task: "Arithmetic Operators"

hackerrank.com/challenges/python-arithmetic-operators/problem

write a program that takes a and b.
- the first line contains the sum of the two numbers
- the second line contains the difference of the two numbers (first - second)
- the third line contains the product of the two numbers
"""


def get_number(instruction):
    """
    Function tha gets the number from the user and catches errors.
    """
    while True:

        try:
            number = int(input(instruction))
            break
        except ValueError:
            print("Not a number")
    return number


a = get_number("input integer for a: ")
b = get_number("input integer for b: ")

print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
