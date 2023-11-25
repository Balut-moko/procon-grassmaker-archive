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


N, Q = map(int, input().split())
A = list(map(lambda x: int(x) + 1, input().split()))

bit = BinarySearchTree(N + 10)
bit_mex = BinarySearchTree(N + 10)

for i in range(N):
    if A[i] <= N + 2:
        bit.insert(A[i])

set_A = set(A)
for i in range(1, N + 3):
    if i not in set_A:
        bit_mex.insert(i)


for _ in range(Q):
    i, x = map(int, input().split())
    i -= 1
    x += 1
    if A[i] <= N + 2:
        bit.erase(A[i])
        if A[i] < bit.minimum(A[i]):
            bit_mex.insert(A[i])
    A[i] = x
    if A[i] <= N + 2:
        if A[i] == bit_mex.minimum(A[i]):
            bit_mex.erase(A[i])
        bit.insert(A[i])
    print(bit_mex.minimum(1) - 1)
