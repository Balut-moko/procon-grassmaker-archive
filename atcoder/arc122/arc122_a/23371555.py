#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * 2 for _ in range(n)]
    mod = 10**9 + 7
    if n == 1:
        print(a[0])
        return
    dp[0][0], dp[0][1], dp[1][0], dp[1][1] = a[0], a[0], a[0], a[0]
    dp[1][0] += a[1]
    dp[1][1] -= a[1]
    tmp_0 = 1
    tmp_1 = 1
    for i in range(2, n):
        tmp = tmp_0
        tmp_0 += tmp_1
        tmp_0 %= mod
        tmp_1 = tmp % mod
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + a[i] * tmp_0) % mod
        dp[i][1] = (dp[i - 1][0] - a[i] * tmp_1) % mod

    print((dp[-1][0] + dp[-1][1]) % mod)


if __name__ == "__main__":
    main()
