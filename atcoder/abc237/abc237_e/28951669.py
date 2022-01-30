from sys import stdin
from collections import deque


def bfs(graph):
    dist = [-1 << 60] * len(graph)
    que = deque([[0, -1]])  # root
    dist[0] = 0
    while que:
        v, p = que.popleft()
        d = dist[v]
        for w, c in graph[v]:
            if w != p:
                if dist[w] < d + c:
                    dist[w] = d + c
                    que.append([w, v])
    return dist


readline = stdin.readline
n, m = map(int, readline().split())
h = list(map(int, readline().split()))
graph = [[] for _ in range(n)]
ans = -1 << 60
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    if h[a] >= h[b]:
        graph[a].append([b, 1 * h[a] - h[b]])
        graph[b].append([a, -2 * (h[a] - h[b])])
    else:
        graph[a].append([b, 2 * (h[a] - h[b])])
        graph[b].append([a, -1 * (h[a] - h[b])])

ans = bfs(graph)
print(max(ans))
