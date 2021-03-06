#!/usr/bin/env python3
import itertools


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cumsum_a = list(itertools.accumulate(reversed(a), initial=0))
    ans = 0
    for i in range(n):
        ans += (n - 1) * a[i] * a[i] - 2 * a[i] * (cumsum_a[n - i - 1])
    print(ans)


if __name__ == "__main__":
    main()
