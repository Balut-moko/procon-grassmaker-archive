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


H, W, Q = map(int, input().split())

s = set()
nxtL = [BinarySearchTree(W) for _ in range(H + 1)]
nxtR = [BinarySearchTree(W) for _ in range(H + 1)]
nxtU = [BinarySearchTree(H) for _ in range(W + 1)]
nxtD = [BinarySearchTree(H) for _ in range(W + 1)]
for r in range(1, H + 1):
    for c in range(1, W + 1):
        nxtL[r].insert(c)
        nxtR[r].insert(c)
        nxtU[c].insert(r)
        nxtD[c].insert(r)

for _ in range(Q):
    r, c = map(int, input().split())
    if (r, c) not in s:
        s.add((r, c))
        nxtL[r].erase(W - c + 1)
        nxtR[r].erase(c)
        nxtU[c].erase(H - r + 1)
        nxtD[c].erase(r)
        continue

    cR = nxtR[r].minimum(c)
    if 1 <= cR <= W:
        s.add((r, cR))
        nxtL[r].erase(W - cR + 1)
        nxtR[r].erase(cR)
        nxtU[cR].erase(H - r + 1)
        nxtD[cR].erase(r)

    cL = nxtL[r].minimum(W - c + 1)
    cL = W - cL + 1
    if 1 <= cL <= W:
        s.add((r, cL))
        nxtL[r].erase(W - cL + 1)
        nxtR[r].erase(cL)
        nxtU[cL].erase(H - r + 1)
        nxtD[cL].erase(r)

    rU = nxtU[c].minimum(H - r + 1)
    rU = H - rU + 1
    if 1 <= rU <= H:
        s.add((rU, c))
        nxtL[rU].erase(W - c + 1)
        nxtR[rU].erase(c)
        nxtU[c].erase(H - rU + 1)
        nxtD[c].erase(rU)

    rD = nxtD[c].minimum(r)
    if 1 <= rD <= H:
        s.add((rD, c))
        nxtL[rD].erase(W - c + 1)
        nxtR[rD].erase(c)
        nxtU[c].erase(H - rD + 1)
        nxtD[c].erase(rD)

print(H * W - len(s))
