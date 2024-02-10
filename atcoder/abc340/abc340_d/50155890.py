from heapq import heappop, heappush


N = int(input())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    A, B, X = map(int, input().split())
    X -= 1
    graph[i].append((i + 1, A))
    graph[i].append((X, B))


INF = 1 << 60
dist = [INF] * len(graph)

start = 0
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

print(dist[-1])
