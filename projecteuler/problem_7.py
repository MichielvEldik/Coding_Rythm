"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime(n):
    """
    input: any number
    output: True or False statement about it being a prime number.
    """
    if n <= 1 or n % 1 > 0:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


COUNTER = 0
holder = []


while COUNTER <= 10:
    for i in range(1, 9999999999):
        if is_prime(i) is True:
            temp_list = [COUNTER, i]
            holder.append(temp_list)
            COUNTER += 1
            if COUNTER == 10003:
                break
print(holder[10001])
