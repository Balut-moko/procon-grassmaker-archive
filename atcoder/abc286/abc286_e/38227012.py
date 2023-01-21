from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
s = [readline()[:-1] for _ in [0] * n]
q = int(readline())
uv = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * q]

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == "Y":
            graph[i].append((j, a[j]))


def bfs(start):
    dist = [[1000, 0] for _ in [0] * n]
    que = deque([start])  # root
    dist[start][0] = 0
    dist[start][1] = a[start]
    while que:
        v = que.popleft()
        d, value = dist[v]
        for w, val in graph[v]:
            if dist[w][0] <= d:
                continue
            dist[w][0] = d + 1
            if dist[w][1] < value + val:
                dist[w][1] = value + val
                que.append(w)
    return dist


dp = [[[0] * 2 for _ in [0] * n] for _ in [0] * n]
for i in range(n):
    for j in range(n):
        dp[i][j][0] = 1000


for i in range(n):
    dist = bfs(i)
    for j in range(n):
        if dp[i][j][0] > dist[j][0]:
            dp[i][j][0] = dist[j][0]
            dp[i][j][1] = max(dp[i][j][1], dist[j][1])

for i in range(q):
    if dp[uv[i][0]][uv[i][1]][0] == 1000:
        print("Impossible")
    else:
        print(*dp[uv[i][0]][uv[i][1]])
