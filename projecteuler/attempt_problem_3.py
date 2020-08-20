"""
Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Prime numbers are natural numbers that are greater than 1
that is not a product of two smaller numbers. 

Approach:
(1) factorise 600851475143
(2) filter out prime numbers
"""


def find_factors(input_number):
    """
    Brute force way of finding factors for a give number.
    It does not work that well for larger numbers.
    That's why I made it break after finding 10 numbers.
    """
    factors_list = []
    for i in range(1, input_number+1):
         if input_number % i == 0:
             factor_list.append(i)
             if len(factor_list) == 10:
                 break
    return factor_list


def efficient_find_factors(input_number):
    """
    Imagine we factorize 24. 
    Notice that 2 x 12 = 24.
    When we found 2 is a factor, we also know that 12 is too!
    This goes for 3 x 8 = 24 and 4 x 6 = 24 as well.
    We don't have to loop all the way to find all factors.
    
    1. Loop 1 to sqrt(number)
    2. if x % i == 0, add i to the list of factors.
    3. e.g. 24 % 2 == 0. so list = [2].
    4. HOWEVER, the answer to 24 / 2 (== 12) can also be added to the list.
    5. so list = [2, 12]
    6. There is one catch: what if i == x/i? (like 16 = 4 x 4) 
    7. We have to handle this case!

    """
    
    # all factors are stored in results
    results = []
    
    # starting point
    i = 1
    
    # step 1
    # loop through all numbers until you reach a number 
    # which has a squareroot that is not <= input_number
    while i*i <= input_number:
        
        # check if i divides by input_number without leaving a remainder
        if input_number % i == 0:
            # append list with this number
            results.append(i)
            
            # if the input number divided by i is not the same as i...
            # append the results list with (input_number // i)
            # handle case explained 
            if input_number //i != i:
                results.append(input_number //i)

        # after all is done, tell computer to move up 1 
        # this continues until it reaches i*i <=! input_number
        i += 1

    # return list with factors
    return results

# flawed way of finding primes
def find_prime_numbers(number_unknown):
    all_primes = []
    length_for_range = number_unknown + 1
    for i in range(2, length_for_range):
        if (number_unknown % i) == 0:
            all_primes.append("T")
        else:
            all_primes.append("F")
           
    if all_primes.count('T') == 1:
        return "It's a prime"
    else:
        return "it's not a prime"


def is_prime(n):
    """
    remember python does not give the last value of range(value).
    So if you do range(7) it will iterate to the number 6.
    This algorithm will return true if it finds zero 'matches'
    Within the range with the exception of the last value.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


def isPrime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for i in range(2, n//2):
      if n % i == 0:
         return False
   return True
print(isPrime(1234169))  
print(isPrime(71)) 


number = 600851475143
factors_list = efficient_find_factors(number)
print(factors_list)
print(factors_list[4])
print(is_prime(factors_list[4]))
for p,  i in enumerate(factors_list):
    if isPrime(i) == True:
        print(p, i)






