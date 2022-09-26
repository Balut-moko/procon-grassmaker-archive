from bisect import bisect_right
from sys import stdin


readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
dp = [0] * (n + 1)

for i in range(n + 1):
    for j in range(k):
        if a[j] > i:
            break
        dp[i] = max(dp[i], i - dp[i - a[j]])

print(dp[n])
