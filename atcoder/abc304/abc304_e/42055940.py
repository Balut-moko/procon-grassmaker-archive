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
uf = UnionFind(n)
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, readline().split())
    uf.union(u, v)

K = int(readline())
xy_roots_set = set()
for _ in range(K):
    x, y = map(lambda x: int(x) - 1, readline().split())
    xr = uf.root(x)
    yr = uf.root(y)
    if xr > yr:
        xr, yr = yr, xr
    xy_roots_set.add((xr, yr))
Q = int(readline())
for _ in range(Q):
    p, q = map(lambda x: int(x) - 1, readline().split())
    pr = uf.root(p)
    qr = uf.root(q)
    if pr > qr:
        pr, qr = qr, pr

    flag = False
    if pr == qr:
        flag = True
    elif (pr, qr) not in xy_roots_set:
        flag = True
    print("Yes" if flag else "No")
