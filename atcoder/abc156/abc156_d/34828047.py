from sys import stdin


def cmb(n, a, mod):
    res = 1
    for i in range(0, a):
        res *= n - i
        res %= mod
    inv = 1
    for i in range(1, a + 1):
        inv *= i
        inv %= mod
    inv = pow(inv, mod - 2, mod)
    return res * inv


readline = stdin.readline
n, a, b = map(int, readline().split())
mod = 10 ** 9 + 7
ans = pow(2, n, mod) - 1
ans -= cmb(n, a, mod)
ans -= cmb(n, b, mod)
print(ans % mod)
