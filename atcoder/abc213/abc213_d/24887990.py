from sys import stdin
from collections import deque


def int1(x):
    return int(x) - 1


readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
ans = []
for i in range(n - 1):
    a, b = map(int1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

stack = deque([])
stack.append([0, -1])  # root
while stack:
    v, p = stack.pop()
    if v >= 0:  # 行きがけの操作
        visited[v] = True
        ans.append(v + 1)
        for e in sorted(graph[v], reverse=True):
            if e == p:
                continue
            if visited[e]:
                continue
            stack.append([-e, v])
            stack.append([e, v])
    else:
        ans.append(p + 1)
print(*ans)
