N, W = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in [0] * N]
max_v = 100001
dp = [1 << 60] * max_v
dp[0] = 0
for w, v in WV:
    ndp = [1 << 60] * max_v
    for i in range(max_v):
        ndp[i] = min(dp[i], ndp[i])
        if i - v < 0:
            continue
        ndp[i] = min(dp[i], dp[i - v] + w)
    dp = ndp

ans = 0
for i in range(max_v):
    if dp[i] <= W:
        ans = i

print(ans)
