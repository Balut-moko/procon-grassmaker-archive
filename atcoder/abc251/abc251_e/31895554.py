from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
dp = [[1 << 60] * 2 for _ in [0] * n]

dp[0][1] = a[0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i]

ans = min(dp[-1][0], dp[-1][1])

dp[0][0] = 0

for i in range(1, n):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i]

ans = min(ans, dp[-1][1])

print(ans)
