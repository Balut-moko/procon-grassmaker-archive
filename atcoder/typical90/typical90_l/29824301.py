from sys import stdin
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


readline = stdin.readline
h, w = map(int, readline().split())
q = int(readline())
uf = UnionFind(h * w + 1)
grid = [[0] * w for _ in range(h)]
dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
for _ in range(q):
    que, *rc = map(lambda x: int(x) - 1, readline().split())
    if que == 0:
        r, c = rc[0], rc[1]
        grid[r][c] = 1
        for x, y in dxy:
            if 0 <= r + x < h and 0 <= c + y < w:
                if grid[r + x][c + y] == 1:
                    uf.union(r * w + c, (r + x) * w + c + y)
    elif que == 1:
        r1, c1, r2, c2 = rc[0], rc[1], rc[2], rc[3]
        ans = "No"
        if grid[r1][c1] == 1 and grid[r2][c2] == 1:
            if uf.same(r1 * w + c1, r2 * w + c2):
                ans = "Yes"
        print(ans)
