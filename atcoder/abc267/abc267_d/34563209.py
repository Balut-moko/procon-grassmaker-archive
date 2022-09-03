from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))

dp = [[-1 << 60] * (m + 1) for _ in [0] * n]

for i in range(n):
    dp[i][0] = 0
dp[0][1] = a[0]

for i in range(1, n):
    for j in range(1, m + 1):
        if i + 1 < j:
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + j * a[i])

ans = -1 << 60
for i in range(n):
    ans = max(ans, dp[i][m])
print(ans)
