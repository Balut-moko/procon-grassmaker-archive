from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
b_max = b[-1] + 1
mod = 998244353
dp = [[0] * b_max for _ in [0] * n]

for j in range(a[0], b[0] + 1):
    dp[0][j] += 1

for i in range(n - 1):
    tmp = 0
    for j in range(b[i + 1] + 1):
        tmp += dp[i][j]
        if a[i + 1] <= j:
            dp[i + 1][j] += tmp
            dp[i + 1][j] %= mod
print(sum(dp[-1]) % mod)
