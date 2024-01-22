N = int(input())
P = list(map(float, input().split()))

dp = [0] * (N + 1)
dp[0] = 1
for i, p in enumerate(P):
    ndp = [0] * (N + 1)
    for j in range(i + 1):
        ndp[j] += dp[j] * (1 - p)
        ndp[j + 1] += dp[j] * p
    dp = ndp
print(sum(dp[(N + 1) // 2 :]))
