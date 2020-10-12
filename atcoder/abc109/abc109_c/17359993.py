#!/usr/bin/env python3
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def main():
    n, x = map(int, input().split())
    X = sorted(list(map(int, input().split())) + [x])
    if n == 1:
        ans = X[1] - X[0]
    else:
        x_dist = [X[i] - X[i - 1] for i in range(1, n + 1)]
        ans = gcd(*x_dist)
    print(ans)


if __name__ == "__main__":
    main()
