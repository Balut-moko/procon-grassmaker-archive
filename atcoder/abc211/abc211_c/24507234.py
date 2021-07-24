from sys import stdin

readline = stdin.readline
s = readline()[:-1]
c = 'chokudai'
mod = 1000000007
dp = [[0] * 8 for _ in [0] * len(s)]
cnt = 0
for i in range(len(s)):
    if s[i] == 'c':
        cnt += 1
    dp[i][0] = cnt

for i in range(1, len(s)):
    for j in range(1, 8):
        dp[i][j] += dp[i - 1][j]
        if s[i] == c[j]:
            dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] %= mod
print(dp[-1][-1])
