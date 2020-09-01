import math
import numpy
import time

start = time.time()


class TriangleNumbersList:
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
    return [e for e in numbers_list if e % 2 == 0 and e % 3 == 0 and e % 5 == 0 and e % 7 == 0 and e % 11 == 0]


def counter(lijssie):
    nieuw_lijssie = []
    for i in lijssie[-1]:
        nieuw_lijssie.append(i)
    lissa = [x[1] for x in lijssie]
    lissa.append(lijssie[-1][0])
    set_list = set(lissa)
    count_list = []
    for i in set_list:
        count_list.append(lissa.count(i) + 1)
    hoi = numpy.prod(count_list)
    return hoi


def rec_2(NUMMY, lijssie, count):
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


primes = sieve(10000)

tri_list = TriangleNumbersList(100_000_000_000_000).list
even_tri_list = return_by_two_three(tri_list)

lijssie = []

for i in even_tri_list:
    rec_2(i, lijssie, 0)
    lijssie = []


end = time.time()
print(end - start)
