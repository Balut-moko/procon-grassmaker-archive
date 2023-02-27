from sys import stdin
from collections import deque


readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n


def dfs(graph):
    stack = deque([])
    stack.append([0, -1])
    cnt = 0
    while stack:
        if cnt >= 10 ** 6:
            return cnt
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            visited[v] = True
            cnt += 1
            for e in graph[v]:
                if e == p:
                    continue
                if visited[e]:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作
            visited[-v] = False
    return cnt


print(dfs(graph))
