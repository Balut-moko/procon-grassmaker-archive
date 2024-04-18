from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (N + 1)
stack = deque([])
stack.append([1, -1])  # root
while stack:
    v, p = stack.pop()
    if v >= 0:  # 行きがけの操作
        dp[v] = 1
        for e in graph[v]:
            if e == p:
                continue
            stack.append([-e, v])
            stack.append([e, v])
    else:  # 帰りがけの操作 caution: use -v
        dp[p] += dp[-v]


ans = [0] * (N + 1)
ans[1] = sum(dp[2:])
stack = deque([])
stack.append([1, -1])  # root
while stack:
    v, p = stack.pop()
    if v >= 0:  # 行きがけの操作
        for e in graph[v]:
            if e == p:
                continue
            ans[e] = ans[v] - 2 * dp[e] + N
            stack.append([-e, v])
            stack.append([e, v])

print(*ans[1:], sep="\n")
