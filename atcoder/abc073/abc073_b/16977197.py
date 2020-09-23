#!/usr/bin/env python3

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        l, r = map(int, input().split())
        ans += r - l + 1
    print(ans)


if __name__ == "__main__":
    main()
