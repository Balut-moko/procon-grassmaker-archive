#!/usr/bin/env python3

def main():
    n = int(input())
    s = input()
    dp = [[0] * (n + 1) for _ in range(7)]
    atcoder = 'atcoder'
    for i, v in enumerate(s):
        for j in range(7):
            dp[j][i + 1] = dp[j][i]
        if v == 'a':
            dp[0][i + 1] += 1
        elif v in atcoder:
            dp[atcoder.index(v)][i + 1] = dp[atcoder.index(v) - 1][i] + dp[atcoder.index(v)][i]
            dp[atcoder.index(v)][i + 1] %= 10**9 + 7
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
