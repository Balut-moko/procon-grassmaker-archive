from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
A = set([int(readline()) for _ in [0] * m])
mod = 10 ** 9 + 7
dp = [0] * (n + 1)
dp[0] = 1
if 1 not in A:
    dp[1] = 1
for i in range(2, n + 1):
    if i not in A:
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod

print(dp[n])
