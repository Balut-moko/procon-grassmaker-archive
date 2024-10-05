from itertools import permutations
from math import sqrt


def calc(p1, p2, s):
    a, b = p1
    c, d = p2
    return sqrt((a - c) * (a - c) + (b - d) * (b - d)) / s


N, S, T = map(int, input().split())

xy = [tuple(map(int, input().split())) for _ in [0] * N]
ans = 1 << 60
for val in permutations(xy):
    dp = [[1 << 60] * 2 for _ in [0] * N]
    p0 = (0, 0)
    p1 = (val[0][0], val[0][1])
    p2 = (val[0][2], val[0][3])
    dp[0][0] = calc(p0, p2, S) + calc(p2, p1, T)
    dp[0][1] = calc(p0, p1, S) + calc(p1, p2, T)
    pre1 = p1
    pre2 = p2
    for i in range(1, N):
        p1 = (val[i][0], val[i][1])
        p2 = (val[i][2], val[i][3])
        dp[i][0] = min(
            dp[i - 1][0] + calc(pre1, p2, S) + calc(p2, p1, T),
            dp[i - 1][1] + calc(pre2, p2, S) + calc(p2, p1, T),
        )
        dp[i][1] = min(
            dp[i - 1][0] + calc(pre1, p1, S) + calc(p1, p2, T),
            dp[i - 1][1] + calc(pre2, p1, S) + calc(p1, p2, T),
        )
        pre1 = p1
        pre2 = p2
    ans = min(ans, min(dp[-1]))

print(ans)
