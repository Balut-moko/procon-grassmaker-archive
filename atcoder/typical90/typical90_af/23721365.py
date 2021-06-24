#!/usr/bin/env python3
def main():
    from itertools import permutations
    from sys import stdin
    readline = stdin.readline
    n = int(readline())
    range_n = range(n)
    a = [tuple(map(int, readline().split())) for _ in [0] * n]
    m = int(readline())
    xy = {tuple(map(int, readline().split())) for _ in [0] * m}
    ans = 10**10
    permutations_n = permutations(range_n, n)
    for val in permutations_n:
        pre = -1
        tmp = 0
        for i, v in enumerate(val):
            x, y = pre + 1, v + 1
            if y < x:
                x, y = y, x
            if (x, y) in xy:
                break
            tmp += a[v][i]
            pre = v
        else:
            if tmp < ans:
                ans = tmp
    print(ans if ans != 10**10 else -1)


if __name__ == "__main__":
    main()
