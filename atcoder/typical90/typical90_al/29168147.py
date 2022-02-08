from sys import stdin
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


readline = stdin.readline
a, b = map(int, readline().split())
ans = lcm(a, b)
print(ans if ans <= 10**18 else "Large")
