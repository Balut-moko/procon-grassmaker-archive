from collections import deque


N = int(input())

graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

if len(graph[1]) == 1:
    print(1)
    exit()

dist = [1] * (N + 1)
max_c = 0
stack = deque([])
stack.append([1, -1])  # root
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
        if p == 1:
            max_c = max(max_c, dist[-v] + 1)
        dist[p] += dist[-v]


print(dist[1] - max_c + 1)
