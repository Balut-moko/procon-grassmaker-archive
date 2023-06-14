from collections import defaultdict
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

    def all_group_members(self):
        group_members = defaultdict(set)
        for member in range(self.n):
            group_members[self.root(member)].add(member)
        return group_members


readline = stdin.readline
n, m, k = map(int, readline().split())

friends = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m]
friend_di = defaultdict(int)
uf = UnionFind(n)
for a, b in friends:
    friend_di[a] += 1
    friend_di[b] += 1
    uf.union(a, b)

blocks = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * k]

block_di = defaultdict(int)
for c, d in blocks:
    if uf.same(c, d):
        block_di[c] += 1
        block_di[d] += 1

all_member = uf.all_group_members()

ans = [0] * n
for i in range(n):
    ans[i] = len(all_member[uf.root(i)]) - block_di[i] - friend_di[i] - 1

print(*ans)
