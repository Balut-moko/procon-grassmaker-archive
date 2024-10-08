N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in [0] * N]

dp[0][1] = A[0]

for i in range(1, N):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + A[i] * 2)
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + A[i])

print(max(dp[-1]))
