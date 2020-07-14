from functools import reduce
#!/usr/bin/env python3

import math


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def main():
    N = int(input())
    T = [int(input()) for i in range(N)]
    ans = lcm_list(T)
    print(ans)


if __name__ == "__main__":
    main()
