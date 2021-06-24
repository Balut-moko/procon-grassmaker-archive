#!/usr/bin/env python3
from itertools import permutations


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(m)]
    ans = 10**10
    for val in permutations(range(n), n):
        pre = -1
        tmp = 0
        for i, v in enumerate(val):
            if (pre + 1, v + 1) in xy or (v + 1, pre + 1) in xy:
                break
            tmp += a[v][i]
            pre = v
        else:
            ans = min(ans, tmp)
    print(ans if ans != 10**10 else -1)


if __name__ == "__main__":
    main()
