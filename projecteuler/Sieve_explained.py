"""
Sieve of Eratosthenes alternative implementation.

1. {max_numbers_to_be_checked}
 We only need to cross out all multiples of numbers up to the square root of 2000000.
 Why? because the multiple of that square root covers the limit (in this case being 2_000_000)
 Any multiple coming after this point has already been covered by previous multiple.

2. {prime_numbers = ... etc.}
Initiate a list with numbers from 2 up to 2000000

3. {if n == -1:}
-1 is a flag to indicate that there is not a prime number.
So it will first continue because there are no -1s to encounter yet. This will soon change.

4. if n > max_numbers_to_be_checked (for all n in prime numbers)

We can quit our loop if we reached all the max numbers to be checked.
This means, if we went through all multiples for the numbers 2 to 1414 (square root of 2_000_000)

5. for x in range(m + m -2, len(prime_numbers), m), (for all n in prime numbers)

For every number in our list of (prime) numbers...
Go from beginning to the end of our numbers list and increment with the number itself.
Every place that you come by, change that spot to -1.

6. m + m - 2
This seems kind of odd. imagine we were on the second cycle (m= 3), would that mean we start from 3 + 3 - 2 = 4?
That wouldn't make sense because 4 + 3 = 7. That's a prime number!
That's because range works with INDEX NUMBERS. Index 4 = # 6 in this list because the list starts at 2.


So if we reach the expression "for x in range(m + m - 2)... etc, it means that we have found a prime number because
otherwise n == -1 would hit continue, which basically means ignoring everything under it continue the loop.

So we just found a prime, e.g. 3. We want to mark off all of its multiples but NOT the prime itself. That's why we use
m + m. So we can move one term ahead! However, because our list starts at 2, we need the "-2" so our index is right.
"""
import math


def sieve(limit):
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


primes = sieve(2_000_000)
print(primes)
print(sum(primes))
