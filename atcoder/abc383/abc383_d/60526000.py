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


N = int(input())

primes = list_primes(10**6)
ans = 0
for a in primes:
    if a**8 <= N:
        ans += 1
    else:
        break

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        a = primes[i]
        b = primes[j]
        if a**2 * b**2 <= N:
            ans += 1
        else:
            break

print(ans)
