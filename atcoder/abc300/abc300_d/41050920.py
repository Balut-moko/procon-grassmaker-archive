from bisect import bisect_left
from sys import stdin

readline = stdin.readline
n = int(readline())


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


primes = list_primes(int(n ** 0.5) + 1)
cnt = 0

for j in range(len(primes)):
    b = primes[j]
    if n < b * b * b:
        break
    for i in range(j):
        a = primes[i]
        if n < a * a * b * b * b:
            break
        for k in range(j + 1, len(primes)):
            c = primes[k]
            if a * a * b * c * c <= n:
                cnt += 1
                continue
            break
print(cnt)
