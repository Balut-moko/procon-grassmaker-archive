from sys import stdin

readline = stdin.readline
a, b, c = map(int, readline().split())

mod = 998244353


def calc(n):
    return n * (n + 1) // 2


ans = calc(a) % mod
ans *= calc(b) % mod
ans *= calc(c) % mod
print(ans % mod)
