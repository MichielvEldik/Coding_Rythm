"""
Find sum of all primes below 2,000,000.
Two alternative ways to implement the Sieve of Eratosthenes algorithm and compute the answer.

"""
import math


def sieve(number):
    prime = [True for i in range(number + 1)]
    p = 2
    while p * p <= number:
        if prime[p] is True:
            for i in range(p * 2, number + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    all_primes = []
    for p in range(number + 1):
        if prime[p]:
            all_primes.append(p)
    print(sum(all_primes))


NUMBER = 2_000_000
sieve(NUMBER)


def sieve_alt(limit):
    max_number_to_be_checked = int(math.sqrt(limit))
    nummies = [x for x in range(2, limit + 1)]
    for n in nummies:
        if n == -1:
            continue
        if n > max_number_to_be_checked:
            break
        m = n
        for x in range(m + m - 2, len(nummies), m):  # m + m - 2 = INDEX 4, equivalent to #6 because nummies starts at 2
            nummies[x] = -1
    return [i for i in nummies if i != -1]


primes = sieve_alt(2_000_000)
print(sum(primes))

