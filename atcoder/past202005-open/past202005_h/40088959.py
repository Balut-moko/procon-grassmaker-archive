from sys import stdin

readline = stdin.readline
n, L = map(int, readline().split())
x = set(map(int, readline().split()))
t1, t2, t3 = map(int, readline().split())
dp = [1 << 60] * (L + 4)
dp[0] = 0
for i in range(L):
    if i in x:
        dp[i + 1] = min(dp[i] + t1 + t3, dp[i + 1])
        dp[i + 2] = min(dp[i] + t1 + t2 + t3, dp[i + 2])
        dp[i + 4] = min(dp[i] + t1 + t2 * 3 + t3, dp[i + 4])
    else:
        dp[i + 1] = min(dp[i] + t1, dp[i + 1])
        dp[i + 2] = min(dp[i] + t1 + t2, dp[i + 2])
        dp[i + 4] = min(dp[i] + t1 + t2 * 3, dp[i + 4])

ans = dp[L]
if L - 1 in x:
    ans = min(dp[L - 1] + t1 // 2 + t2 // 2 + t3, ans)
else:
    ans = min(dp[L - 1] + t1 // 2 + t2 // 2, ans)

if L - 2 in x:
    ans = min(dp[L - 2] + t1 // 2 + t2 // 2 + t2 + t3, ans)
else:
    ans = min(dp[L - 2] + t1 // 2 + t2 // 2 + t2, ans)

if L - 3 in x:
    ans = min(dp[L - 3] + t1 // 2 + t2 // 2 + t2 * 2 + t3, ans)
else:
    ans = min(dp[L - 3] + t1 // 2 + t2 // 2 + t2 * 2, ans)
print(ans)
