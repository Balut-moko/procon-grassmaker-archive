from sys import stdin

readline = stdin.readline
n, p = map(int, readline().split())
if n == 1:
    print(1)
    exit()
mod = 998244353
inv = pow(100, mod - 2, mod)
hh = (p * inv) % mod
h = (1 - hh) % mod
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] += dp[i - 1] * h
    dp[i] += dp[max(0, i - 2)] * hh
    dp[i] += 1
    dp[i] %= mod
print(dp[n])
