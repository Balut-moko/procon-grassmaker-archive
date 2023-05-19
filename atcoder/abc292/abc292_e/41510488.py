from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)

ans = 0


for i in range(n):
    visited = [False] * n
    visited[i] = True
    que = deque([i])
    while que:
        v = que.popleft()
        for w in graph[v]:
            if visited[w]:
                continue
            visited[w] = True
            que.append(w)
            ans += 1
print(ans - m)
