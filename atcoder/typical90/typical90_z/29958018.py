from sys import stdin
from collections import deque


def dfs(graph):
    seen = [-1] * len(graph)
    seen[0] = 1
    stack = deque([])
    stack.append([0, -1])  # root
    while stack:
        v, p = stack.pop()
        if p != -1:
            if seen[p] == 1:
                seen[v] = 0
            else:
                seen[v] = 1
        for e in graph[v]:
            if e == p:
                continue
            stack.append([e, v])
    return seen


readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)
seen = dfs(graph)
ans = [i + 1 for i, val in enumerate(seen) if val == 1]
if len(ans) < n // 2:
    ans = [i + 1 for i, val in enumerate(seen) if val == 0]

print(*ans[: n // 2])
