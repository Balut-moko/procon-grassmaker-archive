#!/usr/bin/env python3
import math


def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    dp = [math.inf] * (n + 1)
    dp[0] = 1
    j = 0
    if m != 0 and a[0] == 1:
        dp[1] = 0
        j += 1
    else:
        dp[1] = 1
    for i in range(2, n + 1):
        if j < m and a[j] == i:
            dp[i] = 0
            j += 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= 1000000007
    print(dp[n])


if __name__ == "__main__":
    main()
