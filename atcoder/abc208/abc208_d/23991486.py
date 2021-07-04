from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

dp = [[1 << 60] * n for _ in [0] * n]
for i in range(n):
    dp[i][i] = 0
for i in range(m):
    a, b, c = map(int, readline().split())
    dp[a - 1][b - 1] = c
answer = 0
for k in range(n):
    nxt = [[0] * n for _ in [0] * n]
    for i in range(n):
        for j in range(n):
            nxt[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if nxt[i][j] < 1 << 59:
                answer += nxt[i][j]
    dp = nxt
print(answer)
