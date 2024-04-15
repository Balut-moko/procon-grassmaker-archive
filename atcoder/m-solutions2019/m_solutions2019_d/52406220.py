from collections import deque
from heapq import heappop, heappush


N = int(input())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

c = sorted(map(int, input().split()), reverse=True)
d = [0] * N

que = deque([0])

i = 0
visited = [False] * len(graph)
visited[0] = True
while que:
    v = que.popleft()
    d[v] = c[i]
    i += 1
    for w in graph[v]:
        if visited[w]:
            continue
        visited[w] = True
        que.append(w)

M = 0
visited = [False] * len(graph)
que = deque([0])  # root
visited[0] = True
while que:
    v = que.popleft()
    for w in graph[v]:
        if visited[w]:
            continue
        M += min(d[v], d[w])
        visited[w] = True
        que.append(w)
print(M)
print(*d)
