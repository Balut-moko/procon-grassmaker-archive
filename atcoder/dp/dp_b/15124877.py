#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    INF = 1 << 60
    dp = [INF] * 100010

    dp[0] = 0

    for i in range(N):
        for j in range(1, K + 1):
            if i + j < N:
                dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
