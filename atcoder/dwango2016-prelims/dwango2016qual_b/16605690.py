#!/usr/bin/env python3

def main():
    n = int(input())
    k = list(map(int, input().split()))
    ans = [1] * n
    ans[0] = k[0]
    ans[-1] = k[-1]
    for i in range(1, n - 1):
        ans[i] = min(k[i], k[i - 1])
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
