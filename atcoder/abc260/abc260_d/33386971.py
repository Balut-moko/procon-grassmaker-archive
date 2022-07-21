from sys import stdin


class SelfBalancingBinarySearchTree:
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


readline = stdin.readline
n, k = map(int, readline().split())
p = list(map(int, readline().split()))

sb = SelfBalancingBinarySearchTree(n)
under = [-1] * (n + 1)
pile = [0] * (n + 1)
ans = [-1] * (n + 1)
for i in range(n):
    x = p[i]
    y = sb.lower_bound(sb.sum(x - 1) + 1)[0]
    if y == n + 1:
        pile[x] = 1
        sb.add(x, 1)
    else:
        under[x] = y
        pile[x] = pile[y] + 1
        sb.add(x, 1)
        sb.add(y, -1)
    if pile[x] == k:
        sb.add(x, -1)
        for j in range(k):
            ans[x] = i + 1
            x = under[x]

print(*ans[1:], sep="\n")
