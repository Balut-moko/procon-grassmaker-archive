class COMmod:
    def __init__(self, n, mod=10**9 + 7) -> None:
        self.fact = [1] * (n + 1)
        self.factInv = [1] * (n + 1)
        self.mod = mod
        r = 1
        for i in range(1, n + 1):
            self.fact[i] = r = r * i % mod
        self.factInv[n] = r = pow(self.fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.factInv[i - 1] = r = r * i % mod

    def perm(self, n, k):
        return self.fact[n] * self.factInv[n - k] % self.mod

    def comb(self, n, k):
        return self.fact[n] * self.factInv[k] * self.factInv[n - k] % self.mod


N, K = map(int, input().split())
B = K
R = N - K

com = COMmod(5000)
MOD = 10**9 + 7
for i in range(1, K + 1):
    if R + 1 < i:
        print(0)
    else:
        print(com.comb(R + 1, i) * com.comb(K - 1, i - 1) % MOD)
