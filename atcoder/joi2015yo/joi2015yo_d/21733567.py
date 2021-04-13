#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    d = [int(input()) for _ in range(n)]
    c = [int(input()) for _ in range(m)]

    dp = [[1 << 60] * (n + 1) for _ in range(m)]
    for i in range(m):
        dp[i][0] = 0
    dp[0][1] = d[0] * c[0]

    for i in range(1, m):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + d[j - 1] * c[i])

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
