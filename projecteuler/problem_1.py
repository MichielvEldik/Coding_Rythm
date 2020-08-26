"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5.
We would get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000
"""
# define list
list_numbers = range(1000)


def returner(list_in, multiple_1, multiple_2):
    """
    Makes a list of all items that meet the condition.
    Returns the sum of these items.
    """
    carry_list = []
    for i in list_in:
        if i % multiple_1 == 0 or i % multiple_2 == 0:
            carry_list.append(i)
    return sum(carry_list)


final_sum = returner(list, 3, 5)
print(final_sum)  # answer:233168
