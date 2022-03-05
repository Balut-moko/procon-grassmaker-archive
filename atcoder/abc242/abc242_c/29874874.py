from sys import stdin

readline = stdin.readline
n = int(readline())
mod = 998244353
dp = [[0] * 9 for _ in [0] * n]

for j in range(9):
    dp[0][j] = 1

for i in range(1, n):
    for j in range(9):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
        elif j == 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        dp[i][j] %= mod

print(sum(dp[-1]) % mod)
