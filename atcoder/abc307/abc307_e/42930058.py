from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
mod = 998244353

print((pow(m - 1, n, mod) + pow(-1, n, mod) * (m - 1)) % mod)
