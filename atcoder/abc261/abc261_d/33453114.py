from collections import defaultdict
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
x = list(map(int, readline().split()))
cy = [tuple(map(int, readline().split())) for _ in [0] * m]
di = defaultdict(int)
for c, y in cy:
    di[c] = y

dp = [[0] * (n + 1) for _ in [0] * n]

for i in range(n):
    for j in range(i + 2):
        if j == 0:
            dp[i][j] = max(dp[i - 1])
            continue
        dp[i][j] = dp[i - 1][j - 1] + x[i] + di[j]

print(max(dp[-1]))
