from math import sqrt


N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(N):
    dp[i + 1] = 0.9 * dp[i] + P[i]
    for j in range(i - 1, -1, -1):
        dp[j + 1] = max(0.9 * dp[j] + P[i], dp[j + 1])

w = 0
ans = -1200
for i in range(1, N + 1):
    w = 0.9 * w + 1
    ans = max(ans, dp[i] / w - 1200 / sqrt(i))

print(ans)
