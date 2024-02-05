N = int(input())
A = list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

dp = [[1 << 60] * (N + 1) for _ in [0] * (N + 1)]
for i in range(N):
    dp[i][i + 1] = 0

for w in range(2, N + 1):
    for i in range(N):
        j = i + w
        if j > N:
            break
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + S[j] - S[i])

print(dp[0][N])
