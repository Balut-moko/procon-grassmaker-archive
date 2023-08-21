from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())

graph = [[] for _ in range(n)]
for i in range(n):
    _, *p = list(map(lambda x: int(x) - 1, readline().split()))
    for v in p:
        graph[i].append(v)

read = [False] * n


def dfs():
    ans = []
    stack = deque([])
    stack.append([0, -1])  # root
    while stack:
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            pass
            for e in graph[v]:
                if e == p:
                    continue
                if read[e]:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作 caution: use -v
            if read[-v]:
                continue
            ans.append(-v + 1)
            read[-v] = True
    return ans


ans = dfs()

print(*ans)
