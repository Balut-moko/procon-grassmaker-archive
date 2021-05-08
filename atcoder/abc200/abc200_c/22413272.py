#!/usr/bin/env python3
import collections
import math


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_mod = list(map(lambda x: x % 200, a))
    ans = 0
    cnt = collections.Counter(a_mod)
    for v in cnt.values():
        if v != 1:
            ans += math.factorial(v) // (math.factorial(v - 2) * math.factorial(2))
    print(ans)


if __name__ == "__main__":
    main()
