#!/usr/bin/env python3

def main():
    n, s, t = map(int, input().split())
    w = 0
    cnt = 0
    for i in range(n):
        w += int(input())
        if s <= w <= t:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
