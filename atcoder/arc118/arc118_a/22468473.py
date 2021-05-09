#!/usr/bin/env python3
import math


def main():
    t, n = map(int, input().split())
    ans = math.floor(n / t * (100 + t))
    if ans == n / t * (100 + t):
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
