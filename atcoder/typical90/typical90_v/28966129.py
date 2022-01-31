from sys import stdin
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


readline = stdin.readline
abc = list(map(int, readline().split()))
cubic = gcd_list(abc)
ans = sum([val // cubic - 1 for val in abc])
print(ans)
