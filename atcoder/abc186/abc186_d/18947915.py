#!/usr/bin/env python3
import itertools


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    cumsum_a = list(itertools.accumulate(a, initial=0))
    ans = 0
    for i in range(1, n):
        ans += i * a[i] - cumsum_a[i]
    print(ans)


if __name__ == "__main__":
    main()
