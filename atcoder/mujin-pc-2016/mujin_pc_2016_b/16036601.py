#!/usr/bin/env python3
import math


def main():
    labc = sorted(map(int, input().split()))
    ans = math.pi * sum(labc)**2
    if labc[2] > labc[0] + labc[1]:
        ans -= math.pi * (labc[2] - labc[0] - labc[1])**2

    print(ans)


if __name__ == "__main__":
    main()
