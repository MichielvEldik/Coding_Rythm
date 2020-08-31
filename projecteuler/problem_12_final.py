import math
import numpy
import sys


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


primes = sieve(100_000_000)
print("Done")
set(primes)
print("DONERONY")

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

tri_limit = 100_000_000
tri_list = TriangleNumbersList(80_576_500).list
# print(tri_list)

treyway = []

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
    global treyway
    if NUMMY == 1:
        lijssie.pop()
        hallo = counter(lijssie)
        moggu = int(hallo)
        treyway.append(moggu)
        return False

    if NUMMY % primes[count] == 0:
        lijssie.append([NUMMY//primes[count], primes[count]])
        rec_2(NUMMY//primes[count], lijssie, 0)
    elif NUMMY % primes[count] != 0:
        rec_2(NUMMY, lijssie, count+1)


lijssie = []
for i in tri_list[4:]:
    rec_2(i, lijssie, 0)
    lijssie = []

for index, i in enumerate(treyway):
    if i >= 400:
        print(index, i)
print(treyway)


