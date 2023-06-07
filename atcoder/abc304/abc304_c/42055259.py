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
N, D = map(int, readline().split())
xy = [tuple(map(int, readline().split())) for _ in [0] * N]

uf = UnionFind(N)

for i in range(N):
    xi, yi = xy[i]
    for j in range(i + 1, N):
        xj, yj = xy[j]
        if (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj) <= D * D:
            uf.union(i, j)

member = set(uf.members(0))

for i in range(N):
    print("Yes" if i in member else "No")
