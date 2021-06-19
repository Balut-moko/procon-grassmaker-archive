#!/usr/bin/env python3
import math


def main():
    n = int(input())
    cost = math.floor(n * 1.08)
    if cost == 206:
        ans = 'so-so'
    elif cost < 206:
        ans = 'Yay!'
    else:
        ans = ':('
    print(ans)


if __name__ == "__main__":
    main()
