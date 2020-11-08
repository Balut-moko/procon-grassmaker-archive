#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cumsum = [0] * (n + 1)
    cumsummax = [0] * (n + 1)
    cumsumsum = [0] * (n + 2)
    ans = 0
    for i in range(n):
        cumsum[i + 1] = cumsum[i] + a[i]
        cumsummax[i + 1] = max(cumsummax[i], cumsum[i + 1])
    for i in range(n + 1):
        cumsumsum[i + 1] = cumsumsum[i] + cumsum[i]
    for i in range(n):
        ans = max(ans, cumsumsum[i + 1] + cumsummax[i + 1])
    print(ans)


if __name__ == "__main__":
    main()
