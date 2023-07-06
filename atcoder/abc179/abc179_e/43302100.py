from sys import stdin

readline = stdin.readline
n, x, m = map(int, readline().split())


nex = [[-1] * m for _ in [0] * 60]
res = [[0] * m for _ in [0] * 60]

for i in range(m):
    nex[0][i] = i * i % m
    res[0][i] = i

for k in range(1, 60):
    for i in range(m):
        nex[k][i] = nex[k - 1][nex[k - 1][i]]
        res[k][i] = res[k - 1][i] + res[k - 1][nex[k - 1][i]]

ans = 0

for k in range(60):
    if n & (1 << k):
        ans += res[k][x]
        x = nex[k][x]
print(ans)
