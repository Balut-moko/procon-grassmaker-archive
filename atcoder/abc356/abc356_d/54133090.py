def has_bit(n, i):
    return n & (1 << i) > 0


def f(j, n):
    res = (n >> (j + 1)) << j
    if has_bit(n, j):
        res += (n & ((1 << j) - 1)) + 1
    return res


N, M = map(int, input().split())
MOD = 998244353

ans = 0
for i in range(60):
    if has_bit(M, i):
        ans += f(i, N)
        ans %= MOD

print(ans)
