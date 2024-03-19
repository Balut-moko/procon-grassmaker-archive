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


N = int(input())
MOD = 10**9 + 7

c = COMmod(N + 1)
for k in range(1, N + 1):
    ans = 0
    for i in range(1, N // k + 11):
        if N - (k - 1) * (i - 1) < i:
            break
        ans += c.comb(N - (k - 1) * (i - 1), i)
        ans %= MOD
    print(ans)
