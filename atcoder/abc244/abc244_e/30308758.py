from sys import stdin


def bfs(graph, s, k, x):
    dp = [[[0] * 2 for _ in [0] * len(graph)] for _ in [0] * (k + 1)]
    dp[0][s][0] = 1
    for i in range(1, k + 1):
        for j, e in enumerate(graph):
            for jj in e:
                if jj != x:
                    dp[i][jj][0] += dp[i - 1][j][0]
                    dp[i][jj][0] %= 998244353
                    dp[i][jj][1] += dp[i - 1][j][1]
                    dp[i][jj][1] %= 998244353
                else:
                    dp[i][jj][0] += dp[i - 1][j][1]
                    dp[i][jj][0] %= 998244353
                    dp[i][jj][1] += dp[i - 1][j][0]
                    dp[i][jj][1] %= 998244353
    return dp


readline = stdin.readline

n, m, k, s, t, x = map(int, readline().split())
s -= 1
t -= 1
x -= 1

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = bfs(graph, s, k, x)
print(dp[k][t][0])
