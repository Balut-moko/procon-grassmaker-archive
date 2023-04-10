from collections import defaultdict, deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n)]

for i in range(n):
    p = int(readline())
    if p == -1:
        root = i
        continue
    graph[p - 1].append(i)

q = int(readline())
que = [[] for _ in range(n)]

for i in range(q):
    a, b = map(lambda x: int(x) - 1, readline().split())
    que[a].append([i, b])

ans = [False] * q
boss = [False] * n


def dfs(i):
    for q, b in que[i]:
        ans[q] = boss[b]
    boss[i] = True
    for j in graph[i]:
        dfs(j)
    boss[i] = False


dfs(root)

for flag in ans:
    print("Yes" if flag else "No")
