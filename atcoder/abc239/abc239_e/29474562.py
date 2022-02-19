from sys import stdin
from collections import deque


def dfs(graph, x):
    val_li = [[val] for val in x]
    stack = deque([])
    stack.append([0, -1])  # root
    while stack:
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            pass
            for e in graph[v]:
                if e == p:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作
            val_li[p] += val_li[-v]
            val_li[p] = sorted(val_li[p], reverse=True)[:20]
    return val_li


readline = stdin.readline
n, q = map(int, readline().split())
x = list(map(int, readline().split()))

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

val_li = dfs(graph, x)

vk = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * q]

for v, k in vk:
    print(val_li[v][k])
