#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [None] * n
    allxor = 0
    for i in range(n):
        allxor ^= a[i]
    for i in range(n):
        ans[i] = allxor ^ a[i]
    print(*ans)


if __name__ == "__main__":
    main()
