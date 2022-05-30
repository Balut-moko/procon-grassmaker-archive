from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, m, k = map(int, readline().split())
dp = [[0] * (m + 1) for _ in [0] * n]
mod = 998244353
if k == 0:
    print(pow(m, n, mod))
    exit()

for j in range(1, m + 1):
    dp[0][j] = 1

for i in range(1, n):
    cumsum = list(accumulate(dp[i - 1]))
    for j in range(1, m + 1):
        dp[i][j] = cumsum[m] - cumsum[min(j + k - 1, m)] + cumsum[max(j - k, 0)]
        dp[i][j] %= mod
print(sum(dp[-1]) % mod)
