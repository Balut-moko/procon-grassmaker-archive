from sys import stdin
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


readline = stdin.readline
t = int(readline())

for _ in range(t):
    n, d, k = map(int, readline().split())
    cycle = lcm(n, d)
    div, mod = divmod((k - 1) * d, cycle)
    print((div + mod) % n)
