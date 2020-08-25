

def Sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    all_primes = []
    for p in range(n + 1):
        if prime[p]:
            all_primes.append(p)
    print(sum(all_primes))


n = 2_000_000
Sieve(n)

