from sys import stdin

readline = stdin.readline
h, n = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

dp = [1 << 60] * (h + 1)
dp[0] = 0
for i in range(h + 1):
    for j in range(n):
        a, b = ab[j]
        dp[min(h, i + a)] = min(dp[min(h, i + a)], dp[i] + b)

print(dp[h])
