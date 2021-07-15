from sys import stdin

readline = stdin.readline
n, p = map(int, readline().split())
mod = 1000000007
print((p - 1) * pow(p - 2, n - 1, mod) % mod)
