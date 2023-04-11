from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

s = int(readline()) - 1
K = int(readline())
t = sorted(map(lambda x: int(x) - 1, readline().split()))

dist_K = [[1 << 60] * (K + 1) for _ in range(K + 1)]
for i in range(K + 1):
    dist_K[i][i] = 0


def bfs(i):
    dist = [None] * len(graph)
    que = deque([i])  # root
    dist[i] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


di = bfs(s)
for j in range(n):
    if j in t:
        dist_K[0][t.index(j) + 1] = di[j]

for i, val in enumerate(t):
    di = bfs(val)
    for j in range(n):
        if j == s:
            dist_K[i + 1][0] = di[j]
        if j in t:
            dist_K[i + 1][t.index(j) + 1] = di[j]


ALL = 1 << (K + 1)

dp = [[1 << 60] * (K + 1) for _ in [0] * ALL]
dp[0][0] = 0


def has_bit(n, i):
    return n & (1 << i) > 0


for n in range(ALL):
    for i in range(K + 1):
        for j in range(K + 1):
            if has_bit(n, j) or i == j:
                continue
            dp[n | (1 << j)][j] = min(dp[n | (1 << j)][j], dp[n][i] + dist_K[i][j])

print(min(dp[ALL - 2]))
