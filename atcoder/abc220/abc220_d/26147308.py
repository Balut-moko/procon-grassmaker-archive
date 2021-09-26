from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
dp = [[0] * 10 for _ in [0] * (n - 1)]
mod = 998244353
dp[0][(a[0] + a[1]) % 10] += 1
dp[0][(a[0] * a[1]) % 10] += 1

for i in range(n - 2):
    for j in range(10):
        idx = (j + a[i + 2]) % 10
        dp[i + 1][idx] += dp[i][j]
        dp[i + 1][idx] %= mod
        idx = (j * a[i + 2]) % 10
        dp[i + 1][idx] += dp[i][j]
        dp[i + 1][idx] %= mod

print(*dp[-1], sep='\n')
