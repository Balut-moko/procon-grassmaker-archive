from sys import stdin

readline = stdin.readline
n, w = map(int, readline().split())
wv = [tuple(map(int, readline().split())) for _ in [0] * n]


dp = [[0] * (w + 1) for _ in [0] * n]
for i, val in enumerate(wv):
    wi, vi = val
    for j in range(w + 1):
        if j - wi >= 0:
            dp[i][j] = max(dp[i - 1][j - wi] + vi, dp[i][j])
        dp[i][j] = max(dp[i - 1][j], dp[i][j])

print(max(dp[-1]))
