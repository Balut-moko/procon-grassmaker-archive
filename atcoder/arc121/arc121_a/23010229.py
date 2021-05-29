#!/usr/bin/env python3
import itertools


def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy = sorted(xy, reverse=True, key=lambda x: x[0])
    tmp = set()
    for i in range(2):
        for j in range(2):
            if i < n - 1 - j:
                tmp.add(xy[i])
                tmp.add(xy[n - 1 - j])
    xy = sorted(xy, reverse=True, key=lambda x: x[1])
    for i in range(2):
        for j in range(2):
            if i < n - 1 - j:
                tmp.add(xy[i])
                tmp.add(xy[n - 1 - j])
    ans = []
    tmp2 = []
    tmp = list(tmp)
    for t in tmp:
        if xy.count(t) != 1:
            tmp2.append(t)
            tmp2.append(t)
        else:
            tmp2.append(t)
    for t in itertools.combinations(tmp2, 2):
        ans.append(max(abs(t[0][0] - t[1][0]), abs(t[0][1] - t[1][1])))

    ans = sorted(ans, reverse=True)
    print(ans[1])


if __name__ == "__main__":
    main()
