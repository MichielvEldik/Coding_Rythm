"""
Divisor algorithm
"""

import math

NUMMY = 300

def sieve(limit):
    """
    generate all prime numbers for a certain number (limit)
    """
    max_number_to_be_checked = int(math.sqrt(limit))
    nummies = [x for x in range(2, limit + 1)]
    for n in nummies:
        if n == -1:
            continue
        if n > max_number_to_be_checked:
            break
        m = n
        for x in range(m + m - 2, len(nummies), m):  # m + m - 2 = INDEX 4 --> #6 and onwards
            nummies[x] = -1
    return [i for i in nummies if i != -1]


primes = sieve(1_000_000)


def recursion(NUMMY, lijssie):
    global primes
    for a in lijssie:
        if a[0] == 1:
            return lijssie

    for i in primes:
        if NUMMY % i == 0:
            lijssie.append([NUMMY//i, i])
            recursion(NUMMY//i, lijssie)
    return lijssie



lijssie = []

print(recursion(24, lijssie))


