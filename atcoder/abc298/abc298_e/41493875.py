from sys import stdin

readline = stdin.readline
n, a, b, p, q = map(int, readline().split())
mod = 998244353
dp = [[[0] * 2 for _ in [0] * (n + 1)] for _ in [0] * (n + 1)]
inv_p = pow(p, mod - 2, mod)
inv_q = pow(q, mod - 2, mod)

for i in range(n):
    dp[n][i][0] = 1
    dp[n][i][1] = 1
    dp[i][n][0] = 0
    dp[i][n][1] = 0

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        for k in range(1, p + 1):
            dp[i][j][0] += dp[min(n, i + k)][j][1]
        dp[i][j][0] *= inv_p
        dp[i][j][0] %= mod
        for k in range(1, q + 1):
            dp[i][j][1] += dp[i][min(n, j + k)][0]
        dp[i][j][1] *= inv_q
        dp[i][j][1] %= mod

print(dp[a][b][0])
