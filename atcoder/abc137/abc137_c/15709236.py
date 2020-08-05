#!/usr/bin/env python3
import collections
import math


def main():
    N = int(input())
    S = ["".join(sorted(input())) for i in range(N)]
    cnt = collections.Counter(S)
    ans = 0
    for v in cnt.values():
        if v != 1:
            ans += math.factorial(v) // (math.factorial(v - 2) * 2)

    print(ans)


if __name__ == "__main__":
    main()
