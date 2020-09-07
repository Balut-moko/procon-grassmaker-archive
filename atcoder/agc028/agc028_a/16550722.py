#!/usr/bin/env python3
import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    ans = lcm(n, m)
    ln = ans // n
    lm = ans // m
    l = lcm(ln, lm)
    i = 0
    while i * l // ln < n and i * l // lm < m:
        if s[i * l // ln] != t[i * l // lm]:
            ans = -1
            break
        i += 1

    print(ans)


if __name__ == "__main__":
    main()
