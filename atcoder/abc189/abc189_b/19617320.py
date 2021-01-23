#!/usr/bin/env python3

def main():
    n, x = map(int, input().split())
    x *= 100
    ans = -1
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p
        if x < 0:
            ans = i + 1
            break
    print(ans)


if __name__ == "__main__":
    main()
