from sys import stdin
from collections import defaultdict


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

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self) -> str:
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]

uf = UnionFind(n)
dx = (-1, -1, 0, 0, 1, 1)
dy = (-1, 0, -1, 1, 0, 1)
for i in range(n):
    for j in range(n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        for k in range(6):
            if x1 - x2 == dx[k] and y1 - y2 == dy[k]:
                uf.union(i, j)
print(uf.group_count())
