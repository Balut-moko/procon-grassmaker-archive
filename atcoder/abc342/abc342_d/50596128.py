from collections import defaultdict
import math


class Osa_k:
    def __init__(self, limit) -> None:
        self.sieve_of_eratosthenes(limit)

    def sieve_of_eratosthenes(self, limit):

        self.sieve = [i for i in range(limit + 1)]

        sqrt_n = math.ceil(math.sqrt(limit))
        for i in range(2, sqrt_n):
            if self.sieve[i] == i:
                for j in range(2 * i, limit + 1, i):
                    self.sieve[j] = i

    def prime_factorization(self, n):
        res = defaultdict(int)
        while n > 1:
            res[self.sieve[n]] += 1
            n //= self.sieve[n]
        return res


N = int(input())
A = list(map(int, input().split()))
fac = Osa_k(2 * 10**5)
sq = [i * i for i in range(1, 1000) if i * i <= 2 * 10**5]
di = defaultdict(int)
for v in A:
    di[v] += 1

ans = 0
for i, ai in enumerate(A):
    di[ai] -= 1
    if ai == 0:
        ans += N - i - 1
        continue
    res = fac.prime_factorization(ai)
    num = 1
    for v, c in res.items():
        if c % 2 != 0:
            num *= v
    for s in sq:
        aj = num * s
        if 2 * 10**5 < aj:
            break
        ans += di[aj]
    ans += di[0]

print(ans)
