#!/usr/bin/env python3

def main():
    l, h = map(int, input().split())
    n = int(input())
    a = [int(input()) for i in range(n)]
    for i in range(n):
        if a[i] < l:
            a[i] = l - a[i]
        elif a[i] <= h:
            a[i] = 0
        else:
            a[i] = -1
    print(*a, sep='\n')


if __name__ == "__main__":
    main()
