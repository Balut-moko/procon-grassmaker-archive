from sys import stdin

readline = stdin.readline
n = int(readline())
a = [tuple(map(int, readline().split())) for _ in [0] * n]
dp = [[0] * 6 for _ in [0] * n]
mod = 10**9 + 7

for j in range(6):
    dp[0][j] = a[0][j]
    dp[0][j] %= mod

for i in range(1, n):
    for j in range(6):
        dp[i][j] = sum(dp[i - 1]) * a[i][j]
        dp[i][j] %= mod

print(sum(dp[-1]) % mod)
