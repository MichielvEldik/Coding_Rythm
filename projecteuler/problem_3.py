"""
Problem 3:

What is the largest prime factor of the number 600851475143?

Approach:

- Function to return all factors for the number in a list.
- Function to determine which of these factors are prime numbers.
- Print the largest prime number
"""


class LargestPrimeFactor:
    """
    Initialize the number first.
    Create a list of all factors for given number.
    Return index and value of every prime number in list of factors.
    """
    def __init__(self, number):
        """
        Initialize number and calls methods find_factor and is_prime
        """
        self.number = number
        factors_list = self.find_factors()
        for p, i in enumerate(factors_list):
            if self.is_prime(i) is True:
                print(p, i)

    def find_factors(self):
        """
        finds all factors and returns a list of them.
        """
        results = []
        i = 1
        while i*i <= self.number:
            if self.number % i == 0:
                results.append(i)
                if self.number // i != i:
                    results.append(self.number // i)
            i += 1
        return results

    def is_prime(self, n):
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


if __name__ == '__main__':
    NUMBER = 600851475143
    LargestPrimeFactor(NUMBER)
