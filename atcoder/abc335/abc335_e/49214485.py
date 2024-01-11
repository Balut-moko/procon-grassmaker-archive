from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)


dist = [None] * len(graph)

start = 0
hq = [(A[0], -1, start)]
while hq:
    a, d, v = heappop(hq)
    if dist[v] is not None:
        continue
    dist[v] = d
    for to in graph[v]:
        if dist[to] is not None:
            continue
        if a == A[to]:
            heappush(hq, (A[to], d, to))
        elif a < A[to]:
            heappush(hq, (A[to], d - 1, to))

if dist[-1] is None:
    print(0)
else:
    print(-dist[N - 1])
