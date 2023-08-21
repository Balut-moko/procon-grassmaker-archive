from sys import stdin, setrecursionlimit


setrecursionlimit(10 ** 6)
readline = stdin.readline
n = int(readline())

graph = [[] for _ in range(n)]
for i in range(n):
    _, *p = list(map(lambda x: int(x) - 1, readline().split()))
    for v in p:
        graph[i].append(v)

read = [False] * n
ans = []


def dfs(i):
    for v in graph[i]:
        if not read[v]:
            dfs(v)
    ans.append(i + 1)
    read[i] = True


dfs(0)

print(*ans[:-1])
