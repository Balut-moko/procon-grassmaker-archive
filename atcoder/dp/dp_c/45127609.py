from sys import stdin

readline = stdin.readline
n = int(readline())
abc = [tuple(map(int, readline().split())) for _ in [0] * n]

dp = [[0] * 3 for _ in [0] * n]

dp[0][0] = abc[0][0]
dp[0][1] = abc[0][1]
dp[0][2] = abc[0][2]

for i in range(1, n):
    a, b, c = abc[i]
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c

print(max(dp[-1]))
