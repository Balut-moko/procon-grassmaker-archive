from sys import stdin

readline = stdin.readline
n, m, K = map(int, readline().split())
mod = 998244353

dp = [[0] * 2600 for _ in [0] * n]
for j in range(1, m + 1):
    dp[0][j] = 1

for i in range(1, n):
    for j in range(1, m + 1):
        for k in range(2501):
            dp[i][k + j] += dp[i - 1][k]
            dp[i][k + j] %= mod

print(sum(dp[-1][: K + 1]) % mod)
