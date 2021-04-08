#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    a = {}
    for i in range(k):
        key, val = map(int, input().split())
        a[key - 1] = val - 1
    dp = [[[0] * 3 for _ in range(3)] for _ in range(101)]
    dp[0][0][0] = 1

    for i in range(n):
        for j in range(3):
            for k in range(3):
                choice = [0, 1, 2]
                if i in a.keys():
                    choice = {a[i]}
                for c in choice:
                    if 2 <= i and j == k == c:
                        continue
                    dp[i + 1][k][c] += dp[i][j][k]

    ans = 0
    for j in range(3):
        for k in range(3):
            ans += dp[n][j][k]
            ans %= 10000
    print(ans)


if __name__ == "__main__":
    main()
