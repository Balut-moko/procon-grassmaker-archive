from sys import stdin
from collections import deque


def bfs(graph):
    dist = [None] * len(graph)
    que = deque([0])  # root
    dist[0] = 1
    while que:
        v = que.popleft()
        for w in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = v + 1
            que.append(w)
    return dist


readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = bfs(graph)
if None in ans:
    print("No")
    exit()
print("Yes")
for i in range(1, n):
    print(ans[i])
