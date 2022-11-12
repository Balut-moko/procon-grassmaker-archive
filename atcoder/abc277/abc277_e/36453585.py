from sys import stdin
from collections import deque


readline = stdin.readline
n, m, k = map(int, readline().split())
uva = [tuple(map(int, readline().split())) for _ in [0] * m]
s_set = set(map(lambda x: int(x) - 1, readline().split()))

graph = [[] for _ in range(n)]

for u, v, a in uva:
    graph[u - 1].append((v - 1, a))
    graph[v - 1].append((u - 1, a))


def bfs(graph):
    dist = [[None] * len(graph) for _ in range(2)]
    que = deque([[0, 1]])  # root
    dist[1][0] = 0
    while que:
        v, flg = que.popleft()
        d = dist[flg][v]
        if v in s_set:
            if dist[not flg][v] is None:
                dist[not flg][v] = d
                que.append([v, not flg])
            elif dist[not flg][v] < d:
                dist[not flg][v] = d
                que.append([v, not flg])

        for w, a in graph[v]:
            if flg == a:
                if dist[a][w] is not None:
                    continue
                dist[a][w] = d + 1
                que.append([w, a])
    return dist


dist = bfs(graph)
ans = 1 << 60
if dist[0][-1] is not None:
    ans = min(ans, dist[0][-1])
if dist[1][-1] is not None:
    ans = min(ans, dist[1][-1])
print(ans if ans != 1 << 60 else -1)
