from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
p = list(map(int, readline().split()))
xy = [tuple(map(int, readline().split())) for _ in [0] * m]

graph = [[] for _ in range(n)]
for i, val in enumerate(p):
    graph[val - 1].append(i + 1)

ans = [False] * n
cnt = [0] * n

for x, y in xy:
    cnt[x - 1] = max(cnt[x - 1], y)


def bfs(s):
    que = deque([s])
    while que:
        v = que.popleft()
        d = cnt[v]
        ans[v] = True
        cnt[v] = 0
        for w in graph[v]:
            cnt[w] = max(cnt[w], d - 1)
            ans[w] = True
            if cnt[w] > 0:
                que.append(w)


for i in range(n):
    if cnt[i] > 0:
        bfs(i)

print(sum(ans))
