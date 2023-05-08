from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

readline = stdin.readline
n = int(readline())
c = list(readline().split())

MOD = 10 ** 9 + 7
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0] * 3 for _ in [0] * n]


def dfs(i, p):
    s = 1
    t = 1
    if c[i] == "a":
        k = 0
    else:
        k = 1

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
