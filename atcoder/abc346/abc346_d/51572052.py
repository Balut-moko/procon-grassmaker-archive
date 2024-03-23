N = int(input())
S = input()
C = list(map(int, input().split()))
INF = 1 << 60
dp = [[[INF] * 2 for _ in [0] * 2] for _ in [0] * N]

if S[0] == "0":
    dp[0][0][0] = 0
    dp[0][0][1] = C[0]
if S[0] == "1":
    dp[0][0][0] = C[0]
    dp[0][0][1] = 0

for i in range(1, N):
    if S[i] == "0":
        dp[i][0][0] = dp[i - 1][0][1]
        dp[i][0][1] = dp[i - 1][0][0] + C[i]
        dp[i][1][0] = min(dp[i - 1][0][0], dp[i - 1][1][1])
        dp[i][1][1] = min(dp[i - 1][1][0], dp[i - 1][0][1]) + C[i]
    if S[i] == "1":
        dp[i][0][0] = dp[i - 1][0][1] + C[i]
        dp[i][0][1] = dp[i - 1][0][0]
        dp[i][1][0] = min(dp[i - 1][0][0], dp[i - 1][1][1]) + C[i]
        dp[i][1][1] = min(dp[i - 1][1][0], dp[i - 1][0][1])

print(min(dp[-1][1]))
