import math
import numpy


def tri_gen():
    """
    Generate triangle numbers
    """
    start = 0
    count = 1
    while True:
        yield int(start + count)
        start = start + count
        count += 1

list = []
for a in tri_gen():
    if a > 99988799:
        break
    list.append(a)

print(list[-1])



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


def rec_2(NUMMY, lijssie, count):
    if NUMMY == 1:
        lijssie.pop()
        return lijssie
    if NUMMY % primes[count] == 0:
     #   print(NUMMY//primes[count], primes[count])
        lijssie.append([NUMMY//primes[count], primes[count]])
        rec_2(NUMMY//primes[count], lijssie, 0)
    elif NUMMY % primes[count] != 0:
        rec_2(NUMMY, lijssie, count+1)


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
    print(count_list)
    print("Answer", numpy.prod(count_list))


primes = sieve(1_000_000)


lijssie = []
print(rec_2(76_576_500, lijssie, 0))
print(lijssie)
counter(lijssie)
