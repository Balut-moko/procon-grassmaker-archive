#!/usr/bin/env python3
import math


def main():
    L = int(input())
    ans = math.factorial(L - 1) // (math.factorial(L - 12) * math.factorial(11))

    print(ans)


if __name__ == "__main__":
    main()
