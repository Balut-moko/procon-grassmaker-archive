#!/usr/bin/env PyPy3
from sys import stdin
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


readline = stdin.readline
a, b = map(int, readline().split())
ans = lcm(a, b)
print(ans if ans <= 10**18 else 'Large')
