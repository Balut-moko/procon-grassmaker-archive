#!/usr/bin/env python3
import collections


def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = collections.Counter(a)

    sq = sorted([i[0] for i in c.items() if i[1] >= 4])
    rec = sorted([i[0] for i in c.items() if i[1] >= 2])
    tmp1, tmp2 = 0, 0
    if sq:
        tmp1 = sq[-1]**2
    if len(rec) >= 2:
        tmp2 = rec[-1] * rec[-2]
    print(max(tmp1, tmp2))


if __name__ == "__main__":
    main()
