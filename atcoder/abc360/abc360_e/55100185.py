N, K = map(int, input().split())
MOD = 998244353
inv_n = pow(N, -1, MOD)
inv_2 = pow(2, -1, MOD)

p = 2 * (N - 1) * inv_n * inv_n % MOD
q = 2 * inv_n * inv_n % MOD
d = 1
for i in range(K):
    d = (1 - p - q) * d + q
    d %= MOD

u = (N + 2) * inv_2 % MOD
print((d + (1 - d) * u) % MOD)
