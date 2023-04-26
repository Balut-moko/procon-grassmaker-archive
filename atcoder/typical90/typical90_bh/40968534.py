from bisect import bisect_left
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))


def lis(li):
    n = len(li)
    dp = [1 << 60] * n
    indexList = [None] * n
    for i, val in enumerate(li):
        idx = bisect_left(dp, val)
        dp[idx] = val
        indexList[i] = idx
    # compile
    targetIndex = max(indexList)
    lis = [0] * (targetIndex + 1)
    for i in range(n - 1, -1, -1):
        if indexList[i] == targetIndex:
            lis[targetIndex] = li[i]
            targetIndex -= 1
    return indexList


idx_a = lis(a)
idx_ar = lis(a[::-1])

ans = 0
for i in range(n):
    ans = max(ans, idx_a[i] + idx_ar[n - i - 1] + 1)
print(ans)
