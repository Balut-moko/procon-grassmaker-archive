from collections import deque


N = int(input())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

MOD = 10**9 + 7

dp = [[0] * N for _ in [0] * 2]

stack = deque([])
stack.append([0, -1])  # root
while stack:
    v, p = stack.pop()
    if v >= 0:  # 行きがけの操作
        dp[0][v] = 1
        dp[1][v] = 1
        for e in graph[v]:
            if e == p:
                continue
            stack.append([-e, v])
            stack.append([e, v])
    else:  # 帰りがけの操作 caution: use -v
        v = -v
        dp[0][p] *= dp[0][v] + dp[1][v]
        dp[0][p] %= MOD
        dp[1][p] *= dp[0][v]
        dp[1][p] %= MOD

print((dp[0][0] + dp[1][0]) % MOD)
