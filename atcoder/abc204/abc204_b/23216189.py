#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for val in a:
        if 10 < val:
            ans += val - 10
    print(ans)


if __name__ == "__main__":
    main()
