from sys import stdin


class Bit:
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


readline = stdin.readline
s = readline()[:-1]
a = "atcoder"
a_di = {v: i + 1 for i, v in enumerate(a)}
s_li = [a_di[v] for v in s]

bit = Bit(8)
ans = 0
for i, v in enumerate(s_li):
    bit.add(v, 1)
    ans += i + 1 - bit.sum(v)
print(ans)
