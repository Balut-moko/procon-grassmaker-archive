N = int(input())
jobs = [tuple(map(int, input().split())) for _ in [0] * N]
jobs.sort()

dp = [[0] * 5001 for _ in [0] * N]
d, c, s = jobs[0]
if c <= d:
    dp[0][c] = s
for i in range(1, N):
    d, c, s = jobs[i]
    for j in range(5001):
        if j < c or d < j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + s)

print(max(dp[-1]))
