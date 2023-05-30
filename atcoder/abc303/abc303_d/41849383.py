from sys import stdin

readline = stdin.readline
x, y, z = map(int, readline().split())
s = readline()[:-1]

dp = [[1 << 60] * 2 for _ in [0] * len(s)]

if s[0] == "A":
    dp[0][0] = y
    dp[0][1] = z + x
else:
    dp[0][0] = x
    dp[0][1] = z + y

for i in range(1, len(s)):
    if s[i] == "A":
        dp[i][0] = min(dp[i - 1][0] + y, dp[i - 1][1] + z + y)
        dp[i][1] = min(dp[i - 1][1] + x, dp[i - 1][0] + z + x)
    else:
        dp[i][0] = min(dp[i - 1][0] + x, dp[i - 1][1] + z + x)
        dp[i][1] = min(dp[i - 1][1] + y, dp[i - 1][0] + z + y)
print(min(dp[-1]))
