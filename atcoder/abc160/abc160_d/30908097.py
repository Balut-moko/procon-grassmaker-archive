from os import sep
from sys import stdin
from collections import deque


def bfs(graph, root):
    dist = [None] * len(graph)
    que = deque([root])  # root
    dist[root] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


readline = stdin.readline
n, x, y = map(int, readline().split())

graph = [[] for _ in range(n)]
graph[x - 1].append(y - 1)
graph[y - 1].append(x - 1)
for i in range(n - 1):
    graph[i].append(i + 1)
    graph[i + 1].append(i)

ans = [0] * n
for i in range(n):
    dist = bfs(graph, i)
    for j, d in enumerate(dist):
        if i < j:
            ans[dist[j]] += 1
print(*ans[1:], sep="\n")
