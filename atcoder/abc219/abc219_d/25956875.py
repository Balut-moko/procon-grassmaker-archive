from sys import stdin

readline = stdin.readline
n = int(readline())
x, y = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

inf = 1 << 60
dp = [[[inf] * (y + 1) for _ in [0] * (x + 1)] for _ in [0] * (n + 1)]
for i in range(n):
    dp[i][0][0] = 0

for i in range(n):
    for j in range(x + 1):
        for k in range(y + 1):
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][max(0, j - ab[i][0])][max(0, k - ab[i][1])] + 1)

if dp[n][x][y] < inf:
    print(dp[n][x][y])
else:
    print(-1)
