from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

readline = stdin.readline
n = int(readline())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0] * n


def dfs(i, pre):
    dp[i] = 1
    for v in graph[i]:
        if v != pre:
            dfs(v, i)
            dp[i] += dp[v]
    return


dfs(0, -1)
ans = 0
for i in range(n):
    ans += dp[i] * (n - dp[i])

print(ans)
