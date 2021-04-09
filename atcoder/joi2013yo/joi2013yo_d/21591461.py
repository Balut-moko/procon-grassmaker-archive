#!/usr/bin/env python3

def main():
    d, n = map(int, input().split())
    t = [int(input()) for _ in range(d)]
    huku = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1 << 60] * n for _ in range(d + 1)]

    for i in range(d):
        for j in range(n):
            if huku[j][0] <= t[i] <= huku[j][1]:
                if i == 0:
                    dp[i + 1][j] = 0
                    continue
                for k in range(n):
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] + abs(huku[k][2] - huku[j][2]))
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
