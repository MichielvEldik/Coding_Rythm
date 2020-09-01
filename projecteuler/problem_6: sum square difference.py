"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def square_numbers(any_number):
    """
    input: any number
    output: squared value of input
    """

    squared_number = any_number**2
    return squared_number


# empty list to hold numbers 1 to 100
NATURAL_NUMBERS = []

# append empty list with numbers 1 to 100
for i in range(1, 101):
    NATURAL_NUMBERS.append(i)

# new variable to hold the sum of all numbers in NATURAL_NUMBERS
sum_of_list = sum(NATURAL_NUMBERS)

# new variable to hold the squareroot of the sum of NATURAL_NUMBERS
sqr_sum_of_list = sum_of_list**2

# empty list to hold a list of all squared values of numbers 1 to 100
SQUARED_LIST = []

# Append empty list with all squared values of the numbers 1 to 100
for i in NATURAL_NUMBERS:
    SQUARED_LIST.append(square_numbers(i))

# variable to hold the sum of all squared values of the numbers 1 to 100
sum_of_sqr_list = sum(SQUARED_LIST)

# print answer
print(sqr_sum_of_list - sum_of_sqr_list)
