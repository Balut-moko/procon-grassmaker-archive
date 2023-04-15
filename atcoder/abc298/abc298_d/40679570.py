from collections import deque
from sys import stdin

MOD = 998244353


class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(self.x * pow(other.x, MOD - 2, MOD))
            if isinstance(other, ModInt)
            else ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD))
            if isinstance(other, ModInt)
            else ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x)
            if isinstance(other, ModInt)
            else ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(other.x * pow(self.x, MOD - 2, MOD))
            if isinstance(other, ModInt)
            else ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD))
            if isinstance(other, ModInt)
            else ModInt(pow(other, self.x, MOD))
        )


readline = stdin.readline
Q = int(readline())
que = deque([1])
s = ModInt(1)
for _ in range(Q):
    t, *x = map(int, readline().split())

    if t == 1:
        s = s * 10 + x[0]
        que.append(x[0])
    if t == 2:
        digit = len(que)
        num = que.popleft()
        s -= ModInt(10) ** (digit - 1) * num
    if t == 3:
        print(s)
