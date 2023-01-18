from sys import stdin
import math


def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False

    return primes


readline = stdin.readline
t = int(readline())

primes = list_primes(3 * 10**6)
primes_set = set(primes)
for _ in range(t):
    n = int(readline())
    for p in primes:
        if n % p != 0:
            continue
        if (n // p) % p == 0:
            q = n // (p * p)
        else:
            q = p
            p = round(math.sqrt(n // q))
        break
    print(p, q)
