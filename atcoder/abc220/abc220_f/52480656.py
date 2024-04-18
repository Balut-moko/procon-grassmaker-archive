import pypyjit
import sys

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [1] * N
ans = [0] * N


def dfs(i, p, d):
    ans[0] += d
    for x in graph[i]:
        if x != p:
            dfs(x, i, d + 1)
            dp[i] += dp[x]


dfs(0, -1, 0)


def dfs2(i, p):
    for x in graph[i]:
        if x != p:
            ans[x] = ans[i] - 2 * dp[x] + N
            dfs2(x, i)


dfs2(0, -1)


print(*ans, sep="\n")
