from collections import defaultdict
from sys import stdin


def mex(a, b, c):
    nums = {0, 1, 2, 3}
    nums.discard(a)
    nums.discard(b)
    nums.discard(c)
    return min(nums)


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
s = readline()[:-1]
MEX = "MEX"
cnt = defaultdict(lambda: (defaultdict(dict)))
for j in range(3):
    for k in range(3):
        cnt[0][MEX[j]][k] = 0
cnt[0][s[0]][a[0]] += 1
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            cnt[i][MEX[j]][k] = cnt[i - 1][MEX[j]][k]
    cnt[i][s[i]][a[i]] += 1

ans = 0
for e in range(1, n - 1):
    if s[e] != "E":
        continue
    for k1 in range(3):
        for k2 in range(3):
            m = cnt[e - 1]["M"][k1]
            x = cnt[n - 1]["X"][k2] - cnt[e]["X"][k2]
            tmp = mex(a[e], k1, k2)
            ans += tmp * m * x
print(ans)
