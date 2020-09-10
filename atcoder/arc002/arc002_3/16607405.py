#!/usr/bin/env python3

def main():
    n = int(input())
    c = input()
    lr = ['AA', 'AB', 'AX', 'AY', 'BA', 'BB', 'BX', 'BY', 'XA', 'XB', 'XX', 'XY', 'YA', 'YB', 'YX', 'YY']
    ans = n
    for L in lr:
        for R in lr:
            dp = [i for i in range(n + 1)]

            for i in range(2, n + 1):
                if c[i - 2:i] == L:
                    dp[i] = min(dp[i - 2] + 1, dp[i - 1] + 1)
                else:
                    dp[i] = min(dp[i], dp[i - 1] + 1)
            for i in range(2, n + 1):
                if c[i - 2:i] == L or c[i - 2:i] == R:
                    dp[i] = min(dp[i - 2] + 1, dp[i - 1] + 1)
                else:
                    dp[i] = min(dp[i], dp[i - 1] + 1)
            ans = min(ans, dp[-1])
    print(ans)


if __name__ == "__main__":
    main()
