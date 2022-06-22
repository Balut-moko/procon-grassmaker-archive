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
x = list(map(lambda x: int(x) - 1, readline().split()))
c = list(map(int, readline().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i].append((x[i], c[i]))

uf = UnionFind(n)
ans = 0
for i in range(n):
    if uf.same(i, x[i]):
        nxt = x[i]
        min_cost = c[i]
        while nxt != i:
            min_cost = min(min_cost, c[nxt])
            nxt = x[nxt]
        ans += min_cost
    uf.union(i, x[i])
print(ans)
