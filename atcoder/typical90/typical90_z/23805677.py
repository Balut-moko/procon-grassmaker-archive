from sys import stdin

readline = stdin.readline
n = int(readline())


def dfs():
    '''
    頂点：n
    辺：n-1
    '''
    from collections import deque

    graph = [[] for _ in [0] * n]
    for i in range(n - 1):
        a, b = map(int, readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    stack = deque([])
    stack.append([0, -1])  # root
    flg = True
    ans = set()
    while stack:
        v, p = stack.pop()
        if v >= 0:  # 行きがけの操作
            if flg:
                ans.add(v + 1)
            flg = not flg
            for e in graph[v]:
                if e == p:
                    continue
                stack.append([-e, v])
                stack.append([e, v])
        else:  # 帰りがけの操作
            flg = not flg
    if len(ans) < n // 2:
        ans = set(range(1, n + 1)) - ans
    return list(ans)


print(*dfs()[:n // 2])
