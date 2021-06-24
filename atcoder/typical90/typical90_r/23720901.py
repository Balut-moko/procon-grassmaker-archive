#!/usr/bin/env python3
import math


def main():
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    for _ in range(q):
        e = int(input()) % t
        thita = math.radians(e / t * 360)
        b = -l / 2 * math.sin(thita)
        z = -l / 2 * math.cos(thita) + l / 2
        a = (x * x + (b - y) * (b - y))**.5
        ans = math.degrees(math.atan2(z, a))
        print(ans)


if __name__ == "__main__":
    main()
