#!/usr/bin/env python3

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += b * (b + 1) // 2 - a * (a - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
