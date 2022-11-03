from collections import defaultdict
from sys import stdin
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


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

g = 0
for val in a:
    g = math.gcd(g, val)
if g > 1:
    print("not coprime")
    exit()

st = set()
osa_k = Osa_k(10 ** 6 + 1)
for val in a:
    di = osa_k.prime_factorization(val)
    for key in di.keys():
        if key in st:
            print("setwise coprime")
            exit()
        st.add(key)

print("pairwise coprime")
