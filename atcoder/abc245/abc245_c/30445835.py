from sys import stdin
from collections import defaultdict


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def members(self, x: int):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members: defaultdict[int, list] = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

uf = UnionFind(n * 2)

for i in range(1, n):
    if abs(a[i] - a[i - 1]) <= k:
        uf.union(i, i - 1)
    if abs(b[i] - b[i - 1]) <= k:
        uf.union(i + n, i - 1 + n)
    if abs(a[i] - b[i - 1]) <= k:
        uf.union(i, i - 1 + n)
    if abs(b[i] - a[i - 1]) <= k:
        uf.union(i + n, i - 1)

ans = "No"
if uf.same(0, n - 1):
    ans = "Yes"
if uf.same(0, 2 * n - 1):
    ans = "Yes"
if uf.same(n, n - 1):
    ans = "Yes"
if uf.same(n, 2 * n - 1):
    ans = "Yes"
print(ans)
