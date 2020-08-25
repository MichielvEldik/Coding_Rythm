"""
Find sum of all primes below 2,000,000

1. all primes up to a certain point (efficiently)
2. sum all of these prime

Sieve of Eratosthenes necessary for optimized generating prime numbers.
"""


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


