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
N, K = map(int, readline().split())
A = list(map(int, readline().split()))
A.sort()
s = set()

hq = [0]
cnt = 200000
while cnt:
    val = heappop(hq)
    for a in A:
        if val + a not in s:
            s.add(val + a)
            heappush(hq, val + a)
    cnt -= 1

s = sorted(s)
print(s[K - 1])
