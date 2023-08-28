from sys import stdin

readline = stdin.readline
D = int(readline())
N = readline()[:-1]
n = len(N)
mod = 10**9 + 7

dp = [[[0] * (D + 1) for _ in [0] * 2] for _ in [0] * (n + 1)]
dp[0][0][0] = 1

for i in range(n):
    for smaller in range(2):
        for j in range(D):
            ni = int(N[i])
            for x in range(10 if smaller else ni + 1):
                nx = (j + x) % D
                dp[i + 1][smaller or x < ni][nx] += dp[i][smaller][j]
                dp[i + 1][smaller or x < ni][nx] %= mod

print(dp[n][0][0] + dp[n][1][0] - 1)
