#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = min(max(a[:2**(n - 1)]), max(a[2**(n - 1):]))
    print(a.index(ans) + 1)


if __name__ == "__main__":
    main()
