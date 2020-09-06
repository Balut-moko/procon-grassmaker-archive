#!/usr/bin/env python3
import math


def main():
    a, b, x = map(int, input().split())

    if a * a * b / 2 <= x:
        ans = math.atan(2 * (a * a * b - x) / (a * a * a))
    else:
        ans = math.pi / 2 - math.atan(2 * x / (a * b * b))

    print(math.degrees(ans))


if __name__ == "__main__":
    main()
