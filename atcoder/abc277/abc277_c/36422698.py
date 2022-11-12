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
uf = UnionFind(n + 10)
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

ab_set = set()
ab_set.add(1)
for a, b in ab:
    ab_set.add(a)
    ab_set.add(b)

d = {v: i for i, v in enumerate(sorted(ab_set))}
dr = {i: v for i, v in enumerate(sorted(ab_set))}

for a, b in ab:
    aa = d[a]
    bb = d[b]
    uf.union(aa, bb)

print(dr[max(uf.members(0))])
