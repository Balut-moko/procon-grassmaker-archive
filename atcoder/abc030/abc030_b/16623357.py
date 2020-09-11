#!/usr/bin/env python3
import itertools


def main():
    n, m = map(int, input().split())
    ans = abs((n % 12) * 30 + 30 * m / 60 - m * 6)
    ans = min(ans, abs(360 - ans))
    print(ans)


if __name__ == "__main__":
    main()
