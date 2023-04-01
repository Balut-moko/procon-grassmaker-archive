from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))


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


bit_a = Bit(n + 1)
bit_b = Bit(n + 1)
ans = 0

for i, p in enumerate(a):
    ans += i - bit_a.sum(p)
    bit_a.add(p, 1)
for i, p in enumerate(b):
    ans += i - bit_b.sum(p)
    bit_b.add(p, 1)

a.sort()
b.sort()

for i in range(n):
    if a[i] != b[i]:
        print("No")
        exit()

for i in range(n - 1):
    if a[i] == a[i + 1]:
        print("Yes")
        exit()


print("Yes" if ans % 2 == 0 else "No")
