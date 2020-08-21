"""
Task: "Python Division"

https://www.hackerrank.com/challenges/python-division/problem

The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
"""


def get_number(instruction):

    while True:

        try:
            number = int(input(instruction))
            break
        except ValueError:
            print("Not a number")
    return number


def integer_division(a, b):
    print(a//b)


def float_division(a, b):
    print(a/b)


a = get_number("input integer for a: ")
b = get_number("input integer for b: ")

integer_division(a, b)
float_division(a, b)
