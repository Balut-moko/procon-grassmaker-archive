from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

black = []
white = set()


def bfs(i, di):
    bb = set()
    dist = [None] * len(graph)
    que = deque([i])  # root
    white.add(i)
    dist[i] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            if d + 1 < di:
                que.append(w)
                white.add(w)
            if d + 1 == di:
                bb.add(w)
    black.append(bb)


k = int(readline())
for _ in range(k):
    pi, di = map(int, readline().split())
    pi -= 1
    if di != 0:
        bfs(pi, di)

for bb in black:
    if not (bb - white):
        print("No")
        exit()

ans = [1] * n
for i in range(n):
    if i in white:
        ans[i] = 0
print("Yes")
print(*ans, sep="")
