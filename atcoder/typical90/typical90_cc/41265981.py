from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())

dp = [[0] * 5002 for _ in [0] * 5002]

for i in range(n):
    a, b = map(int, readline().split())
    dp[a][b] += 1

for i in range(5001):
    for j in range(1, 5001):
        dp[i][j] += dp[i][j - 1]
for i in range(1, 5001):
    for j in range(5001):
        dp[i][j] += dp[i - 1][j]
ans = 0
for i in range(1, 5001):
    for j in range(1, 5001):
        ik = min(i + k, 5000)
        jk = min(j + k, 5000)
        tmp = dp[ik][jk] - dp[ik][j - 1] - dp[i - 1][jk] + dp[i - 1][j - 1]
        ans = max(ans, tmp)
print(ans)
