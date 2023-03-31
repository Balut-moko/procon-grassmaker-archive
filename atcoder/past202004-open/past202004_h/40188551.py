from itertools import product
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]

graph = [[] for _ in range(11)]

for ni, mi in product(range(n), range(m)):
    if s[ni][mi] == "S":
        from_num = 0
    elif s[ni][mi] == "G":
        from_num = 10
    else:
        from_num = int(s[ni][mi])

    graph[from_num].append((ni, mi))

cost = [[1 << 60] * m for _ in [0] * n]

si, sj = graph[0][0]
cost[si][sj] = 0

for k in range(1, 11):
    for i, j in graph[k]:
        for i2, j2 in graph[k - 1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i - i2) + abs(j - j2))

gi, gj = graph[10][0]
ans = cost[gi][gj]
print(ans if ans != 1 << 60 else -1)
