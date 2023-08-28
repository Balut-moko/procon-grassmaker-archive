from itertools import product
from sys import stdin

readline = stdin.readline
A, B = map(int, readline().split())


def solve(s):
    n = len(s)
    dp = [[[0] * 2 for _ in [0] * 2] for _ in [0] * (n + 1)]
    dp[0][0][0] = 1
    for i, smaller, j in product(range(n), (0, 1), (0, 1)):
        max_d = 9 if smaller else int(s[i])
        for x in range(max_d + 1):
            dp[i + 1][smaller or x < max_d][j or x == 4 or x == 9] += dp[i][smaller][j]
    return dp[n][0][1] + dp[n][1][1]


print(solve(str(B)) - solve(str(A - 1)))
