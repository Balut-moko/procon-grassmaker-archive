from bisect import bisect_left


def calc_LISs(lst):
    n = len(lst)
    dp = [1 << 60] * n
    indexList = [None] * n
    for i, val in enumerate(lst):
        idx = bisect_left(dp, val)
        dp[idx] = val
        indexList[i] = idx
    # compile
    targetIndex = max(indexList)
    lis = [0] * (targetIndex + 1)
    for i in range(n - 1, -1, -1):
        if indexList[i] == targetIndex:
            lis[targetIndex] = lst[i]
            targetIndex -= 1
    return lis, indexList


N = int(input())
A = list(map(int, input().split()))
_, L = calc_LISs(A)
_, R = calc_LISs(A[::-1])

ans = 0
for k in range(N):
    ans = max(ans, L[k] + R[N - k - 1] + 1)

print(ans)
