from sys import stdin


class COMmod:
    def __init__(self, n, mod=10**9 + 7) -> None:
        self.fact = [1] * (n + 1)
        self.rfact = [1] * (n + 1)
        self.mod = mod
        r = 1
        for i in range(1, n + 1):
            self.fact[i] = r = r * i % mod
        self.rfact[n] = r = pow(self.fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.rfact[i - 1] = r = r * i % mod

    def perm(self, n, k):
        return self.fact[n] * self.rfact[n - k] % self.mod

    def comb(self, n, k):
        return self.fact[n] * self.rfact[k] * self.rfact[n - k] % self.mod


readline = stdin.readline
x, y = map(int, readline().split())
commod = COMmod(x)
for i in range(x + 1):
    j = y - i * 2
    if x == i + j * 2:
        print(commod.comb(i + j, i))
        exit()
print(0)
