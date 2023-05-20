from collections import defaultdict, deque
from itertools import combinations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
start = []
goal = []
cnt = defaultdict(set)
for i in range(1, n + 1):
    a = int(readline())
    s = list(map(int, readline().split()))
    for val in s:
        cnt[val].add(i)
        if val == 1:
            start.append(i)
        if val == m:
            goal.append(i)


graph = [[] for _ in range(n + 2)]
for i in range(m):
    for a, b in combinations(cnt[i], 2):
        graph[a].append(b)
        graph[b].append(a)

for s in start:
    graph[0].append(s)
for g in goal:
    graph[g].append(n + 1)


def bfs(s):
    dist = [-1] * len(graph)
    que = deque([s])  # root
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] != -1:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


dist = bfs(0)
ans = dist[n + 1]
if ans != -1:
    ans -= 2

print(ans)
