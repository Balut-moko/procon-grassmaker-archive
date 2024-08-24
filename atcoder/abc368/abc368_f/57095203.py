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

osa = Osa_k(max(A))
ans = 0
for a in A:
    fac = osa.prime_factorization(a)
    ans ^= sum(fac.values())
print("Anna" if ans else "Bruno")
