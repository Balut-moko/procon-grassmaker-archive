import sys

sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))
cnt1, cnt2, cnt3 = 0, 0, 0
for a in A:
    if a == 1:
        cnt1 += 1
    elif a == 2:
        cnt2 += 1
    else:
        cnt3 += 1


dp = [[[-1] * 301 for _ in [0] * 301] for _ in [0] * 301]


def rec(i, j, k):
    if dp[i][j][k] >= 0:
        return dp[i][j][k]
    if i + j + k == 0:
        return 0

    res = 0
    if i > 0:
        res += rec(i - 1, j, k) * i
    if j > 0:
        res += rec(i + 1, j - 1, k) * j
    if k > 0:
        res += rec(i, j + 1, k - 1) * k
    res += N
    res /= i + j + k
    dp[i][j][k] = res
    return res


print(rec(cnt1, cnt2, cnt3))
