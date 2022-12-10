from sys import stdin


class BinarySearchTree:
    def __init__(self, n: int, d):
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
n, m, k = map(int, readline().split())
a = list(map(int, readline().split()))
d = {v: i + 1 for i, v in enumerate(sorted(a))}
dr = {i + 1: v for i, v in enumerate(sorted(a))}
bit_lower = BinarySearchTree(n + 1, dr)
bit_upper = BinarySearchTree(n + 1, dr)
ans = [0] * (n - m + 1)
tmp = 0
for i, val in enumerate(sorted(a[:m])):
    if i < k:
        bit_lower.insert(d[val])
        tmp += val
    else:
        bit_upper.insert(d[val])

ans[0] = tmp

for i in range(1, n - m + 1):

    max_idx = bit_lower.lower_bound(k)[0]
    if a[i - 1] <= dr[max_idx]:
        bit_lower.erase(d[a[i - 1]])
        tmp -= a[i - 1]

        if a[i + m - 1] < dr[max_idx]:
            bit_lower.insert(d[a[i + m - 1]])
            tmp += a[i + m - 1]
        else:
            bit_upper.insert(d[a[i + m - 1]])
            idx = bit_upper.lower_bound(1)[0]
            bit_upper.erase(idx)
            bit_lower.insert(idx)
            tmp += dr[idx]

    else:
        bit_upper.erase(d[a[i - 1]])

        if a[i + m - 1] < dr[max_idx]:
            bit_lower.insert(d[a[i + m - 1]])
            tmp += a[i + m - 1]

            idx = bit_lower.lower_bound(k + 1)[0]
            bit_lower.erase(idx)
            bit_upper.insert(idx)
            tmp -= dr[idx]
        else:
            bit_upper.insert(d[a[i + m - 1]])
    ans[i] = tmp
print(*ans)
