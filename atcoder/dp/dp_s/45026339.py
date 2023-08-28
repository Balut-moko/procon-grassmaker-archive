from itertools import product
from sys import stdin

readline = stdin.readline
K = readline()[:-1]
D = int(readline())
n = len(K)
mod = 10 ** 9 + 7
dp = [[[0] * (D + 1) for _ in [0] * 2] for _ in [0] * (n + 1)]
dp[0][0][0] = 1

for i, smaller, j in product(range(n), (0, 1), range(D)):
    max_d = 9 if smaller else int(K[i])
    for x in range(max_d + 1):
        nx = (j + x) % D  # 遷移先
        dp[i + 1][smaller or x < max_d][nx] += dp[i][smaller][j]
        dp[i + 1][smaller or x < max_d][nx] %= mod

print((dp[n][0][0] + dp[n][1][0] - 1) % mod)
