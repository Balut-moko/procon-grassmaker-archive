from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n, m, k = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

hq = []
flags = [-1] * n
for i in range(k):
    p, h = map(int, readline().split())
    p -= 1
    flags[p] = h
    heappush(hq, (-h, p))


while hq:
    h, v = heappop(hq)
    h *= -1
    for w in graph[v]:
        if flags[w] >= h - 1:
            continue
        flags[w] = h - 1
        if h - 1 > 0:
            heappush(hq, (-1 * (h - 1), w))

cnt = 0
ans = []
for i in range(n):
    if flags[i] == -1:
        continue
    cnt += 1
    ans.append(i + 1)
print(cnt)
print(*ans)
