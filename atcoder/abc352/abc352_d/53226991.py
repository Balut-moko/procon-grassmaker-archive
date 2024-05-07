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


N, K = map(int, input().split())
P = list(map(int, input().split()))
di = {v: i + 1 for i, v in enumerate(P)}
mx_q = []
mn_q = []
bit = BinarySearchTree(N + 1)
for k in range(1, K + 1):
    bit.insert(di[k])

mx, _ = bit.lower_bound(K)
ans = mx - bit.minimum(1)

for i in range(N - K):
    bit.erase(di[i + 1])
    bit.insert(di[K + i + 1])
    mx, _ = bit.lower_bound(K)
    ans = min(ans, mx - bit.minimum(1))

print(ans)
