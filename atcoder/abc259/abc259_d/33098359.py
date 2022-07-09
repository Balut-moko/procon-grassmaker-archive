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


def check_two_circle(xyr1, xyr2):
    if (
        (xyr1[2] - xyr2[2]) ** 2
        <= (xyr1[0] - xyr2[0]) ** 2 + (xyr1[1] - xyr2[1]) ** 2
        <= (xyr1[2] + xyr2[2]) ** 2
    ):
        return True
    return False


readline = stdin.readline
n = int(readline())
sx, sy, tx, ty = map(int, readline().split())
xyr = [tuple(map(int, readline().split())) for _ in [0] * n]

s_circle_set = set()
for i in range(n):
    if check_two_circle(xyr[i], (sx, sy, 0)):
        s_circle_set.add(i)
t_circle_set = set()
for i in range(n):
    if check_two_circle(xyr[i], (tx, ty, 0)):
        t_circle_set.add(i)

uf = UnionFind(n)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if check_two_circle(xyr[i], xyr[j]):
            uf.union(i, j)

if uf.same(s_circle_set.pop(), t_circle_set.pop()):
    ans = "Yes"
else:
    ans = "No"
print(ans)
