from sys import stdin
from collections import deque, defaultdict


def bfs(graph, start, p):
    puzzle = defaultdict(int)
    goal = tuple(range(9))
    stack = deque([])
    stack.append([start, p])
    while stack:
        v, p = stack.popleft()
        if p == goal:
            return puzzle[p]
        for e in graph[v]:
            nxt_p = list(p)
            nxt_p[p.index(v)], nxt_p[p.index(e)] = nxt_p[p.index(e)], nxt_p[p.index(v)]
            nxt_p = tuple(nxt_p)
            if puzzle[nxt_p] == 0:
                puzzle[nxt_p] = puzzle[p] + 1
            else:
                if puzzle[p] + 1 < puzzle[nxt_p]:
                    puzzle[nxt_p] = puzzle[p] + 1
                else:
                    continue
            stack.append([e, nxt_p])
    return -1


readline = stdin.readline
m = int(readline())
graph = [[] for _ in range(9)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, readline().split())
    graph[u].append(v)
    graph[v].append(u)
p = list(map(lambda x: int(x) - 1, readline().split()))
for i in range(9):
    if i not in p:
        start = i
        p.append(i)
p = tuple(p)

print(bfs(graph, start, p))
