from sys import stdin, setrecursionlimit
from functools import lru_cache

setrecursionlimit(10**7)
readline = stdin.readline
n, p = map(int, readline().split())
dp = [0] * (n + 1)
mod = 998244353
inv100 = pow(100, mod - 2, mod)


@lru_cache(None)
def f(x):
    if x <= 0:
        return 0
    if dp[x] > 0:
        return dp[x]
    return (1 + f(max(x - 2, 0)) * p * inv100 + f(x - 1) * (100 - p) * inv100) % mod


print(f(n))
