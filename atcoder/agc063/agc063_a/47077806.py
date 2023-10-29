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


N = int(input())
S = input()

bit_a = BinarySearchTree(N + 2)
bit_b = BinarySearchTree(N + 2)
bit = BinarySearchTree(N + 2)
for i in range(N + 1):
    bit.insert(i + 1)

ans = [""] * N
for i, c in enumerate(S):
    if c == "A":
        bit_a.insert(i + 1)
    else:
        bit_b.insert(i + 1)
for i in range(N):
    if i % 2 == 0:
        # Alice
        idx = bit_b.minimum(1)
        bit_b.erase(idx)
        bit.erase(idx)
        idx = bit.minimum(1)
    else:
        # Bob
        idx = bit_a.minimum(1)
        bit_a.erase(idx)
        bit.erase(idx)
        idx = bit.minimum(1)
    if S[idx - 1] == "A":
        ans[i] = "Alice"
    else:
        ans[i] = "Bob"

print(*ans, sep="\n")
