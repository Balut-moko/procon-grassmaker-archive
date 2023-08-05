from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: int(x) - 1, readline().split())
    graph[v].append(u)

ans = []

for i in range(n):
    if len(graph[i]) == 0:
        ans.append(i + 1)

if len(ans) == 1:
    print(ans[0])
else:
    print(-1)
