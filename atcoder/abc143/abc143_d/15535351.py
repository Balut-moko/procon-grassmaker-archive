#!/usr/bin/env python3
import bisect


def main():
    N = int(input())
    L = sorted(map(int, input().split()))
    ans = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            ans += bisect.bisect_right(L, L[a] + L[b] - 1) - b - 1

    print(ans)


if __name__ == "__main__":
    main()
