from sys import stdin
from collections import deque


def dfs(graph, start, end):
    stack = deque([])
    trace = deque([])
    stack.append([start, -1])  # root
    while stack:
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            trace.append(v)
            if v == end:
                break
            for e in graph[v]:
                if e == p:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作
            trace.pop()
    return trace


readline = stdin.readline
n, x, y = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

trace = dfs(graph, x, y)
print(*trace)
