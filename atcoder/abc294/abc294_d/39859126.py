from sys import stdin
from collections import deque


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
n, q = map(int, readline().split())
per = deque(list(range(1, n + 1)))
bst = BinarySearchTree(n + 1)

for _ in range(q):
    e, *x = map(int, readline().split())
    if e == 1:
        p = per.popleft()
        bst.insert(p)
    if e == 2:
        bst.erase(x[0])
    if e == 3:
        print(bst.minimum(1))
