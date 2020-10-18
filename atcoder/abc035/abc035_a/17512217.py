#!/usr/bin/env python3
import math


def main():
    h, w = map(int, input().split())
    a = math.gcd(h, w)
    print("16:9" if h // a == 16 else "4:3")


if __name__ == "__main__":
    main()
