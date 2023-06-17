from heapq import heappop, heappush
from sys import stdin


class BinarySearchTree:
    def __init__(self, n: int):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, x):
        """累積和がx以上になる最小のindexと、その直前までの累積和"""
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_

    def insert(self, i):
        self.add(i, 1)

    def erase(self, i):
        self.add(i, -1)

    def minimum(self, i):
        return self.lower_bound(self.sum(i - 1) + 1)[0]


readline = stdin.readline
n, k, q = map(int, readline().split())
xy = [tuple(map(int, readline().split())) for _ in [0] * q]
xy_sorted = sorted(xy, key=lambda x: x[1])
a = [0] * (n + 1)

d = {v[1]: i + 2 for i, v in enumerate(xy_sorted)}
d[0] = 1
dr = {v: k for k, v in d.items()}

bst1 = BinarySearchTree(q + 2)
bst2 = BinarySearchTree(q + 2)
ans = 0
bst1.add(1, k)
bst2.add(1, n - k)
for x, y in xy:
    pre_ax = a[x]
    a[x] = y
    m = bst1.minimum(0)
    if m <= d[pre_ax]:
        bst1.erase(d[pre_ax])
        ans -= pre_ax

        bst2.insert(d[y])
        M, _ = bst2.lower_bound(n - k + 1)

        bst1.insert(M)
        bst2.erase(M)
        ans += dr[M]
    else:
        bst2.erase(d[pre_ax])

        bst1.insert(d[y])
        ans += y
        m = bst1.minimum(0)
        bst1.erase(m)
        ans -= dr[m]
        bst2.insert(m)
    print(ans)
