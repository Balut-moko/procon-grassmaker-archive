#!/usr/bin/env python3

def main():
    n, s, t = map(int, input().split())
    w = int(input())
    cnt = 1 if s <= w <= t else 0
    for i in range(n - 1):
        w += int(input())
        if s <= w <= t:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
