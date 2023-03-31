from collections import deque
from itertools import product
from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]

graph = [[] for _ in range(n * m)]

for ni, mi in product(range(n), range(m)):
    if s[ni][mi] == "S":
        from_num = 0
    elif s[ni][mi] == "G":
        from_num = 10
    else:
        from_num = int(s[ni][mi])

    for nj, mj in product(range(n), range(m)):
        if s[nj][mj] == "S":
            to_num = 0
        elif s[nj][mj] == "G":
            to_num = 10
        else:
            to_num = int(s[nj][mj])

        if from_num + 1 == to_num:
            cost = abs(ni - nj) + abs(mi - mj)
            graph[ni * m + mi].append((nj * m + mj, cost))

for ni, mi in product(range(n), range(m)):
    if s[ni][mi] == "S":
        start = ni * m + mi


def dijkstra(graph, start):
    inf = 1 << 60
    dist = [inf] * len(graph)
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for to, cost in graph[v]:
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


dist = dijkstra(graph, start)
for ni, mi in product(range(n), range(m)):
    if s[ni][mi] == "G":
        ans = dist[ni * m + mi]
print(ans if ans != 1 << 60 else -1)
