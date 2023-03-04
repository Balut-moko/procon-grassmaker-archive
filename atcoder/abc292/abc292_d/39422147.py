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
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
edges = [0] * n
uf = UnionFind(n)

for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    edges[a] += 1
    uf.union(a, b)


di = {root: 0 for root in uf.roots()}

for i in range(n):
    di[uf.root(i)] += edges[i]

flag = True
for k, v in di.items():
    if uf.size(k) != v:
        flag = False

print("Yes" if flag else "No")
