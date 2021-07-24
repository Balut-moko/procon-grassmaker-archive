from sys import stdin
from collections import deque


def int1(x): return int(x) - 1


readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in [0] * n]
dist = [-1] * n
dist[0] = 0
cnt = [0] * n
cnt[0] = 1
mod = 1000000007
for i in range(m):
    a, b = map(int1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

stack = deque()
stack.append(0)
while stack:
    v = stack.popleft()
    for e in graph[v]:
        if dist[e] == -1:
            dist[e] = dist[v] + 1
            cnt[e] = cnt[v]
            stack.append(e)
        elif dist[e] == dist[v] + 1:
            cnt[e] += cnt[v]
            cnt[e] %= mod
print(cnt[-1])
