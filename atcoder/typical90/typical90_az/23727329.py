from sys import stdin

readline = stdin.readline
n = int(readline())
dice = [tuple(map(int, readline().split())) for _ in [0] * n]

mod = 10**9 + 7
dp = [[0] * 6 for _ in [0] * n]
for j in range(6):
    dp[0][j] = dice[0][j]
for i in range(1, n):
    pre_sum = sum(dp[i - 1])
    for j in range(6):
        dp[i][j] = pre_sum * dice[i][j] % mod

print(sum(dp[-1]) % mod)
