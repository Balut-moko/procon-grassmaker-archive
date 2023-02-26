from sys import stdin

readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
mod = 998244353

dp = [[0] * 2 for _ in [0] * n]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n):
    if ab[i - 1][0] != ab[i][0]:
        dp[i][0] += dp[i - 1][0]
        dp[i][0] %= mod

    if ab[i - 1][1] != ab[i][0]:
        dp[i][0] += dp[i - 1][1]
        dp[i][0] %= mod

    if ab[i - 1][0] != ab[i][1]:
        dp[i][1] += dp[i - 1][0]
        dp[i][0] %= mod

    if ab[i - 1][1] != ab[i][1]:
        dp[i][1] += dp[i - 1][1]
        dp[i][0] %= mod

print(sum(dp[-1]) % mod)
