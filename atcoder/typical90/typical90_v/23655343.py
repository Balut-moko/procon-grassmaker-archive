#!/usr/bin/env python3
from functools import reduce
import math


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


def main():
    a, b, c = map(int, input().split())
    cube = my_gcd(a, b, c)
    ans = (a // cube) + (b // cube) + (c // cube) - 3
    print(ans)


if __name__ == "__main__":
    main()
