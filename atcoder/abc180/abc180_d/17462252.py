#!/usr/bin/env python3

def main():
    x, y, a, b = map(int, input().split())
    cnt = 0
    while x * a < x + b and x * a < y:
        cnt += 1
        x *= a
    cnt += (y - x) // b
    if (y - x) % b == 0:
        cnt -= 1
    print(cnt)


if __name__ == "__main__":
    main()
