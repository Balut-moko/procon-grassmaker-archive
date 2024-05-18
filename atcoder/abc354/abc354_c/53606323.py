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
AC = [tuple(map(int, input().split())) for _ in [0] * N]
d = {v: i + 1 for i, v in enumerate(AC)}
C = [c for a, c in AC]
sorted_C = sorted(C)
C_idx = {v: i + 1 for i, v in enumerate(sorted(C))}
sorted_AC = sorted(AC)

bit = BinarySearchTree(N + 1)

for i in range(N):
    bit.insert(C_idx[AC[i][1]])

ans = []
for a, c in sorted_AC[:-1]:
    bit.erase(C_idx[c])
    mn = bit.minimum(1)
    if c < sorted_C[mn - 1]:
        ans.append(d[(a, c)])

ans.append(d[sorted_AC[-1]])
ans.sort()

print(len(ans))
print(*ans)
