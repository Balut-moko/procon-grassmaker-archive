#!/usr/bin/env python3

def main():
    N = int(input())
    a = list(map(int, input().split()))

    INF = 1 << 60
    dp = [INF] * (N)
    dp[0] = 0

    for i in range(N):
        if i < N-1:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(a[i] - a[i + 1]))
        if i < N-2:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(a[i] - a[i + 2]))
    print(dp[N - 1])


if __name__ == "__main__":
    main()
