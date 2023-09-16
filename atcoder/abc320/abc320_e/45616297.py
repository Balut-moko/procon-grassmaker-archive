from heapq import heapify, heappop, heappush


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


n, m = map(int, input().split())
tws = [tuple(map(int, input().split())) for _ in [0] * m]
heapify(tws)

bit = BinarySearchTree(n)
for i in range(n):
    bit.insert(i + 1)

ans = [0] * n

while tws:
    t, w, s = heappop(tws)
    if w == 0:
        bit.insert(s)
    else:
        idx, _ = bit.lower_bound(1)
        if idx > n:
            continue
        ans[idx - 1] += w
        heappush(tws, (t + s, 0, idx))
        bit.erase(idx)

print(*ans, sep="\n")
