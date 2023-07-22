from sys import stdin

readline = stdin.readline
h, w, n = map(int, readline().split())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * n]
grid = [[0] * w for _ in [0] * h]
for a, b in ab:
    grid[a][b] = 1

dp = [[0] * w for _ in [0] * h]

for i in range(h):
    if not grid[i][0]:
        dp[i][0] = 1
for j in range(w):
    if not grid[0][j]:
        dp[0][j] = 1

for i in range(1, h):
    for j in range(1, w):
        if grid[i][j]:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

print(sum(map(sum, dp)))
