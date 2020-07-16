#!/usr/bin/env python3
from collections import deque


def main():
    d = deque()
    d.extend(list(input()))

    Q = int(input())
    reflag = False

    for i in range(Q):
        query = list(input().split())
        if query[0] == '1':
            reflag = not reflag
        elif (query[1] == '1' and not reflag) or (query[1] == '2' and reflag):
            d.appendleft(query[2])
        else:
            d.append(query[2])

    if reflag:
        print("".join(reversed(d)))
    else:
        print("".join(d))


if __name__ == "__main__":
    main()
