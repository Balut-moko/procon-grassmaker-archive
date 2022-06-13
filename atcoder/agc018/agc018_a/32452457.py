from sys import stdin
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

if max(a) < k:
    print("IMPOSSIBLE")
    exit()
num = gcd(*a)
if num == 1 or k % num == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
