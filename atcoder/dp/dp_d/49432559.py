N, W = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in [0] * N]

dp = [0] * (W + 1)
dp[0] = 0
for w, v in WV:
    ndp = [-1] * (W + 1)
    for i in range(W + 1):
        ndp[i] = max(dp[i], ndp[i])
        if i - w < 0:
            continue
        ndp[i] = max(dp[i], dp[i - w] + v)
    dp = ndp

print(max(dp))
