from sys import stdin

readline = stdin.readline
n, w = map(int, readline().split())
wv = [tuple(map(int, readline().split())) for _ in [0] * n]


dp = [[1 << 60] * 100001 for _ in [0] * n]

for i, val in enumerate(wv):
    wi, vi = val
    if i == 0:
        dp[i][0] = 0
        dp[i][vi] = wi
        continue
    for j in range(100001):
        if j - vi >= 0:
            dp[i][j] = min(dp[i - 1][j - vi] + wi, dp[i][j])
        dp[i][j] = min(dp[i - 1][j], dp[i][j])


for v in range(100000, -1, -1):
    if dp[-1][v] <= w:
        print(v)
        exit()
