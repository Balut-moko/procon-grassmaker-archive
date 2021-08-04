from sys import stdin
from functools import reduce
from math import gcd

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))


def lcm(x, y):
    return (x * y) // gcd(x, y)


def lcm_any(*numbers):
    return reduce(lcm, numbers, 1)


tmp = lcm_any(*a) - 1
ans = sum([tmp % v for v in a])
print(ans)
