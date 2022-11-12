from sys import stdin
from collections import deque


readline = stdin.readline
n, m, k = map(int, readline().split())
uva = [tuple(map(int, readline().split())) for _ in [0] * m]
s_set = set()
if k:
    s_set = set(map(lambda x: int(x) - 1, readline().split()))

graph = [[] for _ in range(n * 2)]


for u, v, a in uva:
    graph[u + a * n - 1].append((v + a * n - 1, 1))
    graph[v + a * n - 1].append((u + a * n - 1, 1))

for s in s_set:
    graph[s + n].append((s, 0))
    graph[s].append((s + n, 0))


def bfs(graph):
    dist = [-1] * len(graph)
    que = deque([n])  # root
    dist[n] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in graph[v]:
            if dist[w] != -1:
                continue
            dist[w] = d + c
            if c == 0:
                que.appendleft(w)
            else:
                que.append(w)
    return dist


dist = bfs(graph)

ans = 1 << 60
if dist[n - 1] != -1:
    ans = min(ans, dist[n - 1])
if dist[-1] != -1:
    ans = min(ans, dist[-1])
print(ans if ans != 1 << 60 else -1)
