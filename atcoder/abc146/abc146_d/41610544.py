from collections import defaultdict, deque
from sys import stdin

readline = stdin.readline
n = int(readline())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * (n - 1)]

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = ab[i]
    graph[a].append(b)
    graph[b].append(a)

k = 0
for i in range(n):
    k = max(k, len(graph[i]))

ans_dict = defaultdict(int)


def bfs():
    visited = [False] * len(graph)
    que = deque([[0, -1]])  # root
    visited[0] = True
    while que:
        v, pc = que.popleft()
        c = 1
        for w in graph[v]:
            if visited[w]:
                continue
            visited[w] = True
            if c == pc:
                c += 1
            ans_dict[(v, w)] = c
            ans_dict[(w, v)] = c
            que.append([w, c])
            c += 1


bfs()
print(k)
for i in range(n - 1):
    print(ans_dict[ab[i]])
