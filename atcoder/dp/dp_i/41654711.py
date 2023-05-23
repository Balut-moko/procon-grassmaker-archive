from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(float, readline().split()))

dp = [[0] * (n + 1) for _ in [0] * n]
dp[0][0] = 1 - p[0]
dp[0][1] = p[0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] * (1 - p[i])

for i in range(1, n):
    for j in range(1, n + 1):
        dp[i][j] += dp[i - 1][j - 1] * p[i]
        dp[i][j] += dp[i - 1][j] * (1 - p[i])

print(sum(dp[-1][(n + 1) // 2 :]))
