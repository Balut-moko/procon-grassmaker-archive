#!/usr/bin/env python3

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    tmp = 1
    cnt = 0
    for i in range(n):
        tmp = a[tmp-1]
        if tmp == 2:
            print(i + 1)
            return
    print(-1)


if __name__ == "__main__":
    main()
