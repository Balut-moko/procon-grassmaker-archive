#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    print('Yes' if ans == 0 else 'No')


if __name__ == "__main__":
    main()
