from sys import stdin

readline = stdin.readline
n, k, d = map(int, readline().split())
a = list(map(int, readline().split()))

a_mod_d = [val % d for val in a]
dp = [[[-1] * d for _ in [0] * (k + 1)] for _ in [0] * (n + 1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(k + 1):
        for dd in range(d):
            if dp[i][j][dd] == -1:
                continue
            dp[i + 1][j][dd] = max(dp[i + 1][j][dd], dp[i][j][dd])

            if j != k:
                dp[i + 1][j + 1][(dd + a[i]) % d] = max(
                    dp[i + 1][j + 1][(dd + a[i]) % d], dp[i][j][dd] + a[i]
                )

print(dp[n][k][0])
