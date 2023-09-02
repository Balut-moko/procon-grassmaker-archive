from sys import stdin


def has_bit(n, i):
    return n & (1 << i) > 0


readline = stdin.readline
n = int(readline())
m = n * (n - 1) // 2
d = [tuple(map(int, readline().split())) for _ in [0] * (n - 1)]
edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((i, j))


ALL = 1 << n
dp = [[0] * ALL for _ in [0] * (m + 1)]
S = []
C = []
dp[0][0] = 0

for i in range(1, m + 1):
    p, v = edges[i - 1]
    for j in range(ALL):
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if has_bit(j, p):
            continue
        if has_bit(j, v):
            continue
        dp[i][j | (1 << p) | (1 << v)] = max(
            dp[i][j | (1 << p) | (1 << v)], dp[i - 1][j] + d[p][v - p - 1]
        )

print(max(dp[-1]))
