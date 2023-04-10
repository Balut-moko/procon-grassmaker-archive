from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n + 1)]

for i in range(n):
    p = int(readline())
    if p == -1:
        root = i + 1
        continue
    graph[p].append(i + 1)

q = int(readline())
que = [[] for _ in range(n + 1)]

for i in range(q):
    a, b = map(int, readline().split())
    que[a].append([i, b])

ans = [False] * q
boss = [False] * (n + 1)

stack = deque()
stack.append(root)  # root

while stack:
    v = stack.pop()
    if v >= 0:  # 行きがけの操作
        for q, b in que[v]:
            ans[q] = boss[b]
        boss[v] = True
        for e in graph[v]:
            stack.append(-e)
            stack.append(e)
    else:  # 帰りがけの操作 caution: use -v
        boss[-v] = False

for flag in ans:
    print("Yes" if flag else "No")
