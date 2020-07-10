#!/usr/bin/env python3

def main():
    N = int(input())
    h = list(map(int, input().split()))

    INF = 1 << 60

    dp = [INF] * 100010

    dp[0] = 0

    for i in range(N):
        if i + 1 < N:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
        if i + 2 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
