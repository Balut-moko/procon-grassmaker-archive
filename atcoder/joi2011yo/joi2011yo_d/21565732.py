#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * 21 for _ in range(100)]
    dp[1][a[0]] = 1
    for i in range(1, n - 1):
        for j in range(21):
            if j + a[i] <= 20:
                dp[i + 1][j] += dp[i][j + a[i]]
            if 0 <= j - a[i]:
                dp[i + 1][j] += dp[i][j - a[i]]
    print(dp[n - 1][a[n - 1]])


if __name__ == "__main__":
    main()
