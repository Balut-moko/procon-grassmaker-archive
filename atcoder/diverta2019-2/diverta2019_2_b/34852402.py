from collections import defaultdict
from sys import stdin
from collections import deque


def bfs(graph, start, dist):
    que = deque([start])  # root
    dist[start] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    return dist


readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]

di = defaultdict(int)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        tmp = (xy[i][0] - xy[j][0], xy[i][1] - xy[j][1])
        di[tmp] += 1

if len(di) == 0:
    print(n)
else:
    print(n - max(di.values()))
