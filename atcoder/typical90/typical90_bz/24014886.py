from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in [0] * n]
for _ in [0] * m:
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
ans = 0
for i, e in enumerate(graph):
    if sum([1 if val < i else 0 for val in e]) == 1:
        ans += 1

print(ans)
