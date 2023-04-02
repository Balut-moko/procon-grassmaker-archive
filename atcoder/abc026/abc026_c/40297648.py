from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

readline = stdin.readline
n = int(readline())

graph = [[] for _ in range(n)]
for i in range(1, n):
    b = int(readline()) - 1
    graph[b].append(i)


def dfs(e):
    if len(graph[e]) == 0:
        return 1
    values = [dfs(i) for i in graph[e]]
    return max(values) + min(values) + 1


print(dfs(0))
