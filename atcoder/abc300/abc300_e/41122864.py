from functools import lru_cache
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 8)
MOD = 998244353
inv5 = pow(5, MOD - 2, MOD)


@lru_cache(maxsize=None)
def calc(n):
    if n > N:
        return 0
    if n == N:
        return 1
    res = 0
    for i in range(2, 7):
        res += calc(i * n)
    return res * inv5 % MOD


readline = stdin.readline
N = int(readline())
print(calc(1) % MOD)
