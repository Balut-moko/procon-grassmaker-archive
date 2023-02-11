from sys import stdin
from collections import deque


readline = stdin.readline
t = int(readline())

for _ in range(t):

    n, m = map(int, readline().split())
    c = list(map(int, readline().split()))
    graph = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(lambda x: int(x) - 1, readline().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(graph):
        pos = [[1 << 60] * n for _ in [1 << 60] * n]
        pos[0][n - 1] = 0
        que = deque([(0, n - 1)])  # root
        while que:
            tak, aoki = que.popleft()
            for wt in graph[tak]:
                for wa in graph[aoki]:
                    if c[wt] != c[wa]:
                        if pos[wt][wa] > pos[tak][aoki] + 1:
                            pos[wt][wa] = pos[tak][aoki] + 1
                            que.append((wt, wa))
        return pos

    pos = bfs(graph)
    print(pos[n - 1][0] if pos[n - 1][0] != 1 << 60 else -1)
