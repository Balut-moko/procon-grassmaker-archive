from sys import stdin
from collections import deque


def bfs(graph):
    dist = [False] * len(graph)
    que = deque([[0, -1]])  # root
    dist[0] = True
    flag = True
    while que:
        v, pre = que.popleft()
        if len(graph[v]) > 3:
            flag = False
        for w in graph[v]:
            if pre == w:
                continue
            if dist[w]:
                flag = False
                continue
            dist[w] = True
            que.append([w, v])
    if not all(dist):
        flag = False
    return flag


readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

print("Yes" if bfs(graph) else "No")
