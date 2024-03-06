import sys

sys.setrecursionlimit(10**7)

N = int(input())
C = list(input().split())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0] * 3 for _ in [0] * N]
MOD = 10**9 + 7

for i, c in enumerate(C):
    if c == "a":
        dp[i][0] = 1
    else:
        dp[i][1] = 1


def dfs(i, p):
    s = 1
    t = 1
    k = 0 if C[i] == "a" else 1

    for v in graph[i]:
        if v == p:
            continue
        dfs(v, i)
        s *= dp[v][k] + dp[v][2]
        t *= dp[v][0] + dp[v][1] + 2 * dp[v][2]
    dp[i][k] = s % MOD
    dp[i][2] = (t - s) % MOD


dfs(0, -1)
print(dp[0][2])
