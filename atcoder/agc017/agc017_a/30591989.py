from sys import stdin

readline = stdin.readline
n, p = map(int, readline().split())
a = list(map(lambda x: int(x) % 2, readline().split()))

dp = [[0] * 2 for _ in [0] * n]
dp[0][0] = 1
dp[0][a[0]] += 1

for i in range(1, n):
    if a[i] == 0:
        dp[i][0] = dp[i - 1][0] * 2
        dp[i][1] = dp[i - 1][1] * 2
    else:
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

print(dp[-1][p])
