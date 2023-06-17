from sys import stdin

readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]

dp = [[0] * 2 for _ in [0] * n]
dp[0][xy[0][0]] = max(0, xy[0][1])


for i in range(1, n):
    x, y = xy[i]
    if x == 0:
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + y, dp[i - 1][1] + y)
        dp[i][1] = dp[i - 1][1]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + y)

print(max(dp[-1]))
