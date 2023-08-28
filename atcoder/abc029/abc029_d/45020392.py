from itertools import product
from sys import stdin

readline = stdin.readline
N = readline()[:-1]
n = len(N)
D = 10
dp = [[[0] * (D + 1) for _ in [0] * 2] for _ in [0] * (n + 1)]
dp[0][0][0] = 1

for i, smaller, j in product(range(n), (0, 1), range(D)):
    max_d = 9 if smaller else int(N[i])
    for x in range(max_d + 1):
        nx = j + 1 if x == 1 else j
        dp[i + 1][smaller or x < max_d][nx] += dp[i][smaller][j]

ans = 0
for i in range(10):
    ans += (dp[n][0][i] + dp[n][1][i]) * i
print(ans)
