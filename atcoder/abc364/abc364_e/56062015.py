N, X, Y = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in [0] * N]

dp = [[[1 << 60] * (X + 1) for _ in [0] * (N + 1)] for _ in [0] * (N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(i + 1):
        for k in range(X + 1):
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            if k + AB[i][0] <= X:
                dp[i + 1][j + 1][k + AB[i][0]] = min(
                    dp[i + 1][j + 1][k + AB[i][0]], dp[i][j][k] + AB[i][1]
                )

for j in range(N, -1, -1):
    for k in range(X + 1):
        if dp[N][j][k] <= Y:
            print(min(j + 1, N))
            exit()
