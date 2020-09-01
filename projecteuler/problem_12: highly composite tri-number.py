"""
My implementation of project Euler problem 12.
It's a lot of code but also, it's quite fast.

1. Create a list of triangle numbers with an arbitrary large length

2. Sieve the list. so only numbers that can be divided by the first few prime numbers remain in the list.
Why? A highly composite number must be, by definition, divisible by lots of different numbers. Hence, numbers that
can't even divide evenly by 2, 3, 5, 7, or 11 aren't interesting to try. We can filter them out.

3. For our filtered list, we use a recursive function to compute number of divisors
"""
import math
import numpy
import time

start = time.time()


class TriangleNumbersList:
    """ Generate triangle numbers"""
    def __init__(self, limit):
        self.limit = limit
        self.list = []
        for a in self.tri_gen():
            if a > self.limit:
                break
            self.list.append(a)

    def tri_gen(self):
        start = 0
        count = 1
        while True:
            yield int(start + count)
            start = start + count
            count += 1


def sieve(limit):
    """ Generate prime numbers"""
    max_number_to_be_checked = int(math.sqrt(limit))
    nummies = [x for x in range(2, limit + 1)]
    for n in nummies:
        if n == -1:
            continue
        if n > max_number_to_be_checked:
            break
        m = n
        for x in range(m + m - 2, len(nummies), m):
            nummies[x] = -1
    return [i for i in nummies if i != -1]


def return_by_two_three(numbers_list):
    """ filter out numbers that can't divide by the first few prime numbers."""
    return [e for e in numbers_list if e % 2 == 0 and e % 3 == 0 and e % 5 == 0 and e % 7 == 0 and e % 11 == 0]


def counter(lijssie):
    """ Count divisors with prime factorization trick"""
    lissa = [x[1] for x in lijssie]
    lissa.append(lijssie[-1][0])
    count_list = []
    for i in set(lissa):
        count_list.append(lissa.count(i) + 1)
    return numpy.prod(count_list)


def rec_2(NUMMY, lijssie, count):
    """ recursive

    >> Part 1 <<
    This function takes a number (e.g. 78) and tries to divide it evenly by prime numbers.
    It will first try to divide it by the first prime number (78 // 2 = 39).
    In this case, it works! it will now launch itself with the output (39) to try it again.
        Meanwhile, lijssie = [[39, 2]]
    This time, //2 does not work. So it tries the next prime number, 3. (39 // 3 = 13)
    This works! So now it launches itself again with input 13.
        Meanwhile, lijssie = [[39, 2], [13, 3]]
    This will not reach any other prime number than itself, for which the quotient will always be 1.
        Meanwhile lijssie = [[39, 2], [13, 3], [1, 3]]

    >> Part 2 <<
    Once it notices that the input for the function == 1, it will stop trying with the divisors.
    It then pops the last element of lijssie.
        lijssie = [[39, 2], [13, 3]] --> POP [1, 3] because it's not interesting.
    Then, counter function is called with the lijssie.
    Counter returns # of divisors for a number.
    The function ends when this >= 500, which is our answer!
    """
    if NUMMY == 1:
        lijssie.pop()
        hallo = counter(lijssie)
        if int(hallo) >= 500:  # answer: 76576500
            print(lijssie[0][0] * lijssie[0][1])
        return False

    if NUMMY % primes[count] == 0:
        lijssie.append([NUMMY//primes[count], primes[count]])
        rec_2(NUMMY//primes[count], lijssie, 0)

    elif NUMMY % primes[count] != 0:
        try:
            rec_2(NUMMY, lijssie, count+1)
        except RecursionError:
            return False


# create a list of primes. They will be used in our recursive function
primes = sieve(10000)

# list triangle numbers up to an arbitrarily large
tri_list = TriangleNumbersList(100_000_000).list
even_tri_list = return_by_two_three(tri_list)

# empty list that will hold nodes temporarily
lijssie = []

# launch our recursive function
for i in even_tri_list:
    rec_2(i, lijssie, 0)
    lijssie = []


# timing stuff
end = time.time()
print(end - start)

# approx. 0.023533 seconds for n = 100_000_000
# approx. 1.4729 seconds for n = 100_000_000_000
# approx 64.829 seconds for n = 100_000_000_000_000
