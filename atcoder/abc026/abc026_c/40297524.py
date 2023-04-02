from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())

graph = [[] for _ in range(n)]
for i in range(1, n):
    b = int(readline()) - 1
    graph[i].append(b)
    graph[b].append(i)

dp = [1] * n


def dfs(graph):
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
        else:  # 帰りがけの操作 caution: use -v
            mx, mn = 0, 1 << 60
            for e in graph[-v]:
                if e == p:
                    continue
                mx = max(mx, dp[e])
                mn = min(mn, dp[e])
            if mn == 1 << 60:
                mn = 0
            dp[-v] = mx + mn + 1


dfs(graph)

mx, mn = 0, 1 << 60
for e in graph[0]:
    mx = max(mx, dp[e])
    mn = min(mn, dp[e])
if mn == 1 << 60:
    mn = 0
dp[0] = mx + mn + 1

print(dp[0])
