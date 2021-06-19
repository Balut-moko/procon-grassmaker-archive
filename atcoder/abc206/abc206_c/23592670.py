#!/usr/bin/env python3
import collections


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = collections.Counter(a)
    ans = 0
    for i in range(n):
        ans += n - cnt[a[i]]
    print(ans // 2)


if __name__ == "__main__":
    main()
