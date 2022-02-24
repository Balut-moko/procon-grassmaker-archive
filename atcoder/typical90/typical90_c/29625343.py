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
n = int(readline())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist = bfs(graph, 0)
new_root = dist.index(max(dist))
dist = bfs(graph, new_root)
print(max(dist) + 1)
