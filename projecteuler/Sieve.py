"""
Sieve of Eratosthenes implementation.
"""


def prime_list(n, illegal_list):
    for e in illegal_list:
        if n % e == 0:
            return False
    if n <= 1 or n % 1 > 0:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True
all_primes = []
illegal_list = []

for i in range(1, 1_999_999):
    if prime_list(i, illegal_list) is True:
        illegal_list.append(i)
        all_primes.append(i)
        print(i)

print(sum(all_primes))
# print(illegal_list)