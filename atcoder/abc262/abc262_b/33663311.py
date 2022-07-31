from itertools import product
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)
ans = 0
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if a in graph[b] and b in graph[c] and c in graph[a]:
                ans += 1
print(ans)
