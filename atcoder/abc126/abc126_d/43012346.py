from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, w = map(lambda x: int(x) - 1, readline().split())
    w += 1
    graph[a].append((b, w))
    graph[b].append((a, w))

color = [False] * n
color[0] = True


def dfs():
    stack = deque([])
    stack.append([0, -1])  # root
    while stack:
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            for e, ew in graph[v]:
                if e == p:
                    continue
                if ew % 2 == 0:
                    color[e] = color[v]
                else:
                    color[e] = not color[v]
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作 caution: use -v
            pass


dfs()

for val in color:
    print(1 if val else 0)
