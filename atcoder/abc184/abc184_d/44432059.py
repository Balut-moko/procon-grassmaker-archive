from sys import stdin
from functools import lru_cache

readline = stdin.readline
A, B, C = map(int, readline().split())

dp = [[[0] * 101 for _ in [0] * 101] for _ in [0] * 101]


@lru_cache(None)
def f(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if max(a, b, c) == 100:
        return 0
    ans = 0
    ans += (f(a + 1, b, c) + 1) * a / (a + b + c)
    ans += (f(a, b + 1, c) + 1) * b / (a + b + c)
    ans += (f(a, b, c + 1) + 1) * c / (a + b + c)
    return ans


print(f(A, B, C))
