from sys import stdin

readline = stdin.readline
n, m, k = map(int, readline().split())
mod = 998244353
m_inv = pow(m, mod - 2, mod)
dp = [[0] * (n + 1) for _ in [0] * (k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(n):
        for mm in range(1, m + 1):
            jj = j + mm
            if j + mm > n:
                jj = n - jj + n
            dp[i][jj] += dp[i - 1][j] * m_inv
            dp[i][jj] %= mod

dp = list(zip(*dp))
print(sum(dp[-1]) % mod)
