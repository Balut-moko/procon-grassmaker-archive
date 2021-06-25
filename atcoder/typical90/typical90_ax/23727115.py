from sys import stdin

readline = stdin.readline
n, l = map(int, readline().split())
mod = 10**9 + 7
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    dp[i] += dp[i - 1]
    if 0 <= i - l:
        dp[i] += dp[i - l]
    dp[i] %= mod
print(dp[-1])
