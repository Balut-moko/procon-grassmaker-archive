from collections import deque
from sys import stdin


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def root(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        return -self.parents[self.root(x)]

    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def members(self, x: int):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())


readline = stdin.readline
n = int(readline())
q = int(readline())
query = [tuple(map(int, readline().split())) for _ in [0] * q]

graph = [[] for _ in range(n + 1)]
for i in range(q):
    t, x, y, v = query[i]
    if t == 0:
        graph[x].append((y, v))

dist = [[None] * 2 for _ in range(n + 1)]


def bfs(i, s):
    que = deque([i])  # root
    dist[i][s] = s
    while que:
        v = que.popleft()
        d = dist[v][s]
        for w, c in graph[v]:
            if dist[w][s] is not None:
                continue
            dist[w][s] = c - d

            que.append(w)
    return dist


for i in range(n):
    if dist[i][0] is None:
        bfs(i, 0)
        bfs(i, 1)


uf = UnionFind(n + 1)

for i in range(q):
    t, x, y, v = query[i]
    if t == 0:
        uf.union(x, y)
    if t == 1:
        if not uf.same(x, y):
            print("Ambiguous")
            continue
        d = v - dist[x][0]
        if (x - y) % 2 == 0:
            ans = dist[y][0] + d
        else:
            ans = dist[y][0] - d
        print(ans)
