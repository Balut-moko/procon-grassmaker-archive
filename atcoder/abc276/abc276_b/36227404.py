from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph[1:]:
    ans = sorted(g)
    print(len(ans), *ans)
