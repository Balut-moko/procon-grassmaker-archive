from sys import stdin

readline = stdin.readline
a, b, c, d, e, f = map(int, readline().split())
mod = 998244353
print((a * b * c - d * e * f) % mod)
