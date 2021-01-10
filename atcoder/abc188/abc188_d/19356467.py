#!/usr/bin/env python3
import itertools


def main():
    n, C = map(int, input().split())
    event = []
    for i in range(n):
        a, b, c = map(int, input().split())
        a -= 1
        event.append((a, c))
        event.append((b, -c))
    event.sort()
    ans = 0
    money = 0
    d = 0
    for i, j in event:
        if i != d:
            ans += min(money, C) * (i - d)
            d = i
        money += j
    print(ans)


if __name__ == "__main__":
    main()
