from sys import stdin


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

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
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
aa = a + a
mod = 10 ** 9 + 7
bit1 = Bit(2001)
bit2 = Bit(2001)
inv_num1 = 0

for i, p in enumerate(a):
    bit1.add(p, 1)
    inv_num1 += i + 1 - bit1.sum(p)

if k == 1:
    print(inv_num1)
    exit()

inv_num2 = 0
for i, p in enumerate(aa):
    bit2.add(p, 1)
    inv_num2 += i + 1 - bit2.sum(p)

ans = (inv_num2 - inv_num1 * 2) * k * (k - 1) // 2
ans += inv_num1 * k
ans %= mod
print(ans)
