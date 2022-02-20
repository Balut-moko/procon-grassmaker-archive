from sys import stdin
from collections import deque


def dfs(graph):
    ans_li = [[] for _ in range(len(graph))]

    stack = deque([])
    stack.append([0, -1])  # root
    ans_li[0] = [1, 1]
    e_cnt = 1
    while stack:
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            for e in graph[v]:
                if e == p:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作
            if len(ans_li[-v]) == 0:
                ans_li[-v] = [e_cnt, e_cnt]
                e_cnt += 1
            if len(ans_li[p]) == 0:
                ans_li[p] = ans_li[-v]
            ans_li[p] = [
                min(ans_li[-v][0], ans_li[p][0]),
                max(ans_li[-v][1], ans_li[p][1]),
            ]
    return ans_li


readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans_li = dfs(graph)

for ans in ans_li:
    print(*ans)
