from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(lambda x: int(x) - 1, readline().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i].append(a[i])

dist = [None] * len(graph)


def bfs(s):
    que = deque([s])  # root
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] is not None:
                return w
            dist[w] = d + 1
            que.append(w)
    return -1


for i in range(n):
    if dist[i] is None:
        res = bfs(i)
        if res != -1:
            break


def dfs_trace(start, end):
    stack = deque([])
    trace = deque([])
    stack.append([start, -1])  # root
    while stack:
        v, p = stack.pop()
        trace.append(v)
        if v == end and p != -1:
            break
        for e in graph[v]:
            stack.append([e, v])
    return trace


trace = dfs_trace(res, res)

ans = []
for val in trace:
    ans.append(val + 1)

print(len(ans) - 1)
print(*ans[:-1])
