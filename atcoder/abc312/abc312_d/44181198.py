from sys import stdin

readline = stdin.readline
s = readline()[:-1]
mod = 998244353
dp = [[0] * (len(s) + 1) for _ in [0] * len(s)]

if s[0] == ")":
    print(0)
    exit()

dp[0][1] = 1

for i in range(1, len(s)):
    for j in range(len(s)):
        if s[i] == "(":
            if j != 0:
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= mod
        elif s[i] == ")":
            dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= mod
        else:
            dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= mod
            if j != 0:
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= mod

print(dp[-1][0])
