class UnionFindWithPotential:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n
        self.diff_weight = [0] * n

    def root(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            r = self.root(self.parents[x])
            self.diff_weight[x] += self.diff_weight[self.parents[x]]
            self.parents[x] = r
            return self.parents[x]

    def union(self, x: int, y: int, w: int) -> bool:
        w += self.weight(x)
        w -= self.weight(y)

        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x
            w = -w

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.diff_weight[y] = w
        return True

    def weight(self, x: int):
        self.root(x)
        return self.diff_weight[x]

    def diff(self, x: int, y: int):
        return self.weight(y) - self.weight(x)

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
        from collections import defaultdict

        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self) -> str:
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


N, Q = map(int, input().split())

uf = UnionFindWithPotential(N)
ans = []
for i in range(Q):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    if uf.same(a, b):
        if uf.diff(a, b) == d:
            ans.append(i + 1)
    else:
        uf.union(a, b, d)
        ans.append(i + 1)

print(*ans)
