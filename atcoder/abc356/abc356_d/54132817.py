def has_bit(n, i):
    return n & (1 << i) > 0


def f(i, n):
    res = (n >> (i + 1)) << i
    if has_bit(n, i):
        res += n & ((1 << i) - 1) + 1
    return res


def f2(j, n):
    p2 = 1 << j
    k = n // (2 * p2)
    res = k * p2
    l = n % (2 * p2)
    if l >= p2:
        res += l - p2 + 1
    return res


N, M = map(int, input().split())
MOD = 998244353

ans = 0
for i in range(60):
    if has_bit(M, i):
        ans += f2(i, N)
        ans %= MOD

print(ans)
