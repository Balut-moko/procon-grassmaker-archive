#!/usr/bin/env python3
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def main():

    a, b, c, d = map(int, input().split())
    a -= 1
    cd = lcm(c, d)
    ans = b - a - (b // c - a // c) - (b // d - a // d) + (b // cd - a // cd)

    print(ans)


if __name__ == "__main__":
    main()
