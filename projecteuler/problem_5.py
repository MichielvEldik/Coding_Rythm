"""
Problem 5:

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Approach:

- we don't need to go through 1 to 20 for every try. 
- take out 1; every integer is evenly divisble by 1 so there is no point in cumputing this.
- take out 2, 4, 5.  any integer divisible by 20 is also evenly divisble by 2, 4, 5. 
- So if number % 20 == 0 works, we know for sure that number % 2, 4, 5 works too. 
- leave 19 in, it's a prime number.
- leave 18 in but remove its factors 3 and 6. If it's divisible by 18, it will be for 3 and 6 too.
- repeat this process and we end up with a pretty short list.
"""


def isDivisble(number):
    """
    input: any number
    output: True/False for whether it's evenly divisible by 1:20.
    """
    for i in [11, 13, 14, 16, 17, 18, 19, 20]:
        if number % i != 0:
            return False
    return True


# Anything below 20 will never be evenly divisble by 20.
NUMBER = 20


while True:
    if isDivisble(NUMBER):
        break
    # The final number must be evenly divisible by 20.
    # There is no point in incrementing with anything < 20.
    NUMBER += 20
print(NUMBER)
