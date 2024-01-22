N = int(input())
p = list(map(float, input().split()))

dp = [[0] * (N + 1) for _ in [0] * (N + 1)]

dp[0][0] = 1 - p[0]
dp[0][1] = p[0]

for i in range(1, N):
    for j in range(i + 1):
        dp[i][j] += dp[i - 1][j] * (1 - p[i])
        dp[i][j + 1] += dp[i - 1][j] * p[i]

print(sum(dp[N - 1][(N + 1) // 2 :]))
