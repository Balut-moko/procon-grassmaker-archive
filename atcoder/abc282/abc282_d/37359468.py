from collections import defaultdict, deque
from sys import stdin


# 2grarh check
def dfs(graph, colors, start):
    stack = deque([])
    di = {1: 0, -1: 0}
    stack.append([start, 1])
    while stack:
        v, color = stack.pop()
        if colors[v] == 0:
            di[color] += 1
            colors[v] = color
            for to in graph[v]:
                if colors[to] == color:
                    return False, colors, di
                if colors[to] == 0:
                    stack.append([to, -color])
    return True, colors, di


readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = n * (n - 1) // 2 - m
colors = defaultdict(int)
for i in range(n):
    if colors[i] == 0:
        flg, colors, di = dfs(graph, colors, i)
        if not flg:
            print(0)
            exit()
        ans -= di[1] * (di[1] - 1) // 2
        ans -= di[-1] * (di[-1] - 1) // 2
print(ans)
