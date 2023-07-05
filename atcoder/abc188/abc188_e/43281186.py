from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = [1 << 59] + list(map(int, readline().split()))

graph = [[] for _ in range(n + 1)]
graph_r = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, readline().split())
    graph[u].append(v)
    graph_r[v].append(u)

for i in range(1, n + 1):
    graph[0].append(i)

pre_min = [1 << 60] * (n + 1)
hq = [(1 << 60, 0)]
while hq:
    c, v = heappop(hq)
    c *= -1
    if pre_min[v] < c:
        continue
    for to in graph[v]:
        cost = min(pre_min[v], a[v])
        if cost < pre_min[to]:
            pre_min[to] = cost
            heappush(hq, (-cost, to))
ans = -1 << 60
for i in range(1, n + 1):
    ans = max(ans, a[i] - pre_min[i])

print(ans)
