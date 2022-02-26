from sys import stdin


class SelfBalancingBinarySearchTree:
    def __init__(self, n):
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


readline = stdin.readline
q = int(readline())
que = [tuple(map(int, readline().split())) for _ in [0] * q]
num_li = [q[1] for q in que]
num_li.sort()
num_li_dec = sorted(num_li, reverse=True)
n = len(num_li)
bit_inc = SelfBalancingBinarySearchTree(n)
bit_dec = SelfBalancingBinarySearchTree(n)

d = {v: i + 1 for i, v in enumerate(num_li)}
d_dec = {v: i + 1 for i, v in enumerate(num_li_dec)}

for q in que:
    if q[0] == 1:
        bit_inc.add(d[q[1]], 1)
        bit_dec.add(d_dec[q[1]], 1)
    if q[0] == 2:
        pos, _ = bit_dec.lower_bound(bit_dec.sum(d_dec[q[1]] - 1) + q[2])
        if pos > n:
            print(-1)
        else:
            print(num_li_dec[pos - 1])
    if q[0] == 3:
        pos, _ = bit_inc.lower_bound(bit_inc.sum(d[q[1]] - 1) + q[2])
        if pos > n:
            print(-1)
        else:
            print(num_li[pos - 1])
