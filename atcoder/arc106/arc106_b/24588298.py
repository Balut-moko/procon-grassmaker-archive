from sys import stdin
from collections import defaultdict

readline = stdin.readline


def int1(x):
    return int(x) - 1


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def size(self, x):
        return -self.root[self.Find_Root(x)]

    def members(self, x):
        root = self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        all_group_members = defaultdict(list)
        for member in range(self.n):
            all_group_members[self.Find_Root(member)].append(member)
        return all_group_members

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
ans = 'Yes'
Union = UnionFind(n)
for i in range(m):
    c, d = map(int1, readline().split())
    Union.Unite(c, d)
for val in Union.all_group_members().values():
    cnt = 0
    for v in val:
        cnt += a[v] - b[v]
    if cnt != 0:
        ans = 'No'
        break
print(ans)
