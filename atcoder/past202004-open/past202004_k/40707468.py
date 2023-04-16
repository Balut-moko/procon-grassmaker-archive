from itertools import product
from sys import stdin

readline = stdin.readline
N = int(readline())
S = readline()[:-1]
C = list(map(int, readline().split()))
D = list(map(int, readline().split()))
INF = 1 << 60
dp = [[INF] * 2 * N for _ in [0] * N]
if S[0] == "(":
    dp[0][1] = 0
else:
    dp[0][1] = C[0]
dp[0][0] = D[0]


for i, j in product(range(1, N), range(N)):
    if S[i] == "(":
        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + D[i])
        dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + C[i])
    else:
        dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + D[i])
        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + C[i])
print(dp[-1][0])
