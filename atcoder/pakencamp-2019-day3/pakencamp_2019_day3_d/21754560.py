#!/usr/bin/env python3

def main():
    n = int(input())
    S = [list(input()) for _ in range(5)]
    S = list(zip(*S))
    dp = [[1 << 60] * 3 for _ in range(n)]
    color = ['R', 'B', 'W']
    for j in range(3):
        dp[0][j] = 5 - S[0].count(color[j])
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + 5 - S[i].count(color[j])
    print(min(dp[-1]))


if __name__ == "__main__":
    main()
