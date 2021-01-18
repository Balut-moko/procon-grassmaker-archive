#!/usr/bin/env python3
from collections import Counter


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    ans = 0
    for i in range(n):
        if cnt[i] < k:
            ans += i * (k - cnt[i])
            k = cnt[i]
        if k == 0:
            break
    print(ans)


if __name__ == "__main__":
    main()
