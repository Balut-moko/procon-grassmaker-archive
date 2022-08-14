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
n, m, e = map(int, readline().split())
uv = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * e]
q = int(readline())
x = [int(readline()) - 1 for _ in [0] * q]
x_set = set(x)
uf = UnionFind(n + 1)
for i, val in enumerate(uv):
    if not (i in x_set):
        uf.union(min(val[0], n), min(val[1], n))
ans = []
ans.append(uf.size(n) - 1)
for que in x[::-1]:
    u, v = uv[que]
    uf.union(min(u, n), min(v, n))
    ans.append(uf.size(n) - 1)

ans.reverse()
print(*ans[1:], sep="\n")
