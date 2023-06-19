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


readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]

uf = UnionFind(h * w)
black = defaultdict(int)
white = defaultdict(int)

dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
for r in range(h):
    for c in range(w):
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if s[r][c] == s[nr][nc]:
                continue
            uf.union(r * w + c, nr * w + nc)

for r in range(h):
    for c in range(w):
        root = uf.root(r * w + c)
        if s[r][c] == "#":
            black[root] += 1
        else:
            white[root] += 1

ans = 0
for k in black.keys():
    ans += black[k] * white[k]

print(ans)
