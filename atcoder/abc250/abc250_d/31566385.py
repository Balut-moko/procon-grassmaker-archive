from sys import stdin


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
n = int(readline())
primes = list_primes(10**6 + 1)
ans = 0
for q in primes:
    q3 = q * q * q
    for p in primes:
        if not (p < q):
            break
        if p * q3 <= n:
            ans += 1
        else:
            break

print(ans)
