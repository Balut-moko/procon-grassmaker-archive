"""
DP復元
"""

from sys import stdin

readline = stdin.readline
n, s = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

dp = [[False] * (s + 1) for _ in [0] * (n + 1)]
prev = [[0] * n for _ in [0] * s]

dp[0][0] = True

for i in range(1, n + 1):
    a, b = ab[i - 1]
    for j in range(s + 1):
        if j - a >= 0:
            dp[i][j] = dp[i][j] or dp[i - 1][j - a]
        if j - b >= 0:
            dp[i][j] = dp[i][j] or dp[i - 1][j - b]

if not dp[n][s]:
    print("Impossible")
    exit()

ans = ""
cur = s
for i in range(n, -1, -1):
    a, b = ab[i - 1]
    if cur - a >= 0 and dp[i - 1][cur - a]:
        ans += "A"
        cur -= a
        continue
    if cur - b >= 0 and dp[i - 1][cur - b]:
        ans += "B"
        cur -= b
        continue

print(ans[::-1])
