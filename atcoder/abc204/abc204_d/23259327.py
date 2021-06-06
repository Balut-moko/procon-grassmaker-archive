#!/usr/bin/env python3

def main():
    n = int(input())
    t = list(map(int, input().split()))
    k = sum(t) + 1

    dp = [[False] * k for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(n):
        for j in range(k):
            if j - t[i] >= 0:
                dp[i + 1][j] = (dp[i + 1][j] or dp[i][j - t[i]])
            dp[i + 1][j] = (dp[i + 1][j] or dp[i][j])
    for j in range(k // 2, k):
        if dp[n][j]:
            ans = j
            break

    print(ans)


if __name__ == "__main__":
    main()
