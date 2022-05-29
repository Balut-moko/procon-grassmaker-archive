from sys import stdin
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


readline = stdin.readline
n, a, b = map(int, readline().split())

a_max = n // a
b_max = n // b

ab = lcm(a, b)
ab_max = n // ab

ans = (
    n * (n + 1) // 2
    - a * a_max * (a_max + 1) // 2
    - b * b_max * (b_max + 1) // 2
    + ab * ab_max * (ab_max + 1) // 2
)
print(ans)
