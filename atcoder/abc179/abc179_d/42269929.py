from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
lr = [tuple(map(int, readline().split())) for _ in [0] * k]
mod = 998244353
dp = [0] * n
sdp = [0] * (n + 1)
dp[0] = 1
sdp[1] = 1

for i in range(1, n):
    for l, r in lr:
        ll = max(0, i - r)
        rr = max(0, i - l + 1)
        dp[i] += sdp[rr] - sdp[ll]
        dp[i] %= mod
    sdp[i + 1] = sdp[i] + dp[i]
    sdp[i + 1] %= mod

print(dp[-1])
