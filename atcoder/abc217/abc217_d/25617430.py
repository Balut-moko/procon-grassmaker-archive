from sys import stdin
import bisect


class Bit:
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
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos, sum_


readline = stdin.readline
l, q = map(int, readline().split())
ans = []
query = []
x_set = set()
for _ in [0] * q:
    c, x = map(int, readline().split())
    query.append((c, x))
    x_set.add(x)

x_li = [0] + sorted(x_set) + [l]
d = {v: i for i, v in enumerate(x_li)}

bit = Bit(len(d))
bit.add(d[0] + 1, 1)
bit.add(d[l] + 1, 1)
for c, x in query:
    if c == 1:
        bit.add(d[x] + 1, 1)
    else:
        idx1, cumsum1 = bit.lower_bound(bit.sum(d[x]) + 1)
        idx2, cumsum2 = bit.lower_bound(bit.sum(d[x]))
        ans.append(x_li[idx1] - x_li[idx2])
print(*ans, sep='\n')
