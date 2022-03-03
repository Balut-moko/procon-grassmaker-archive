from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
mod = 10**9 + 7
atcoder = "atcoder"
d = {v: i for i, v in enumerate(atcoder)}
dp = [[0] * 7 for _ in [0] * n]

if s[0] == "a":
    dp[0][0] += 1


for i in range(1, n):
    for j in range(7):
        dp[i][j] = dp[i - 1][j]
        if s[i] in d.keys():
            if d[s[i]] == 0:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][0] %= mod
            elif j == d[s[i]]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                dp[i][j] %= mod

print(dp[-1][-1])
