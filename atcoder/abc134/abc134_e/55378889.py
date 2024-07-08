from bisect import bisect_right


def calc_LISs(lst):
    n = len(lst)
    dp = [1 << 60] * n
    indexList = [None] * n
    for i, val in enumerate(lst):
        idx = bisect_right(dp, val)
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
A = [int(input()) for _ in [0] * N]
A.reverse()
lis, idxLst = calc_LISs(A)
print(len(lis))
