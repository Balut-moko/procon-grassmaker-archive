#!/usr/bin/env python3
import queue


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = queue.deque()
    for i in range(n):
        if i % 2 == 1:
            q.appendleft(a[i])
        else:
            q.append(a[i])
    if n % 2 == 1:
        q.reverse()
    print(*q, sep=" ")


if __name__ == "__main__":
    main()
