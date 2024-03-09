def search(s: str):
    res = []
    cur = 0
    while True:
        idx = T[cur:].find(s)
        if idx == -1:
            return res
        res.append(idx + cur)
        cur = idx + cur + 1


T = input()
N = int(input())
dp = [1 << 60] * (len(T) + 1)
dp[0] = 0
for i in range(N):
    A, *S = input().split()
    ndp = dp[:]
    for s in S:
        lst = search(s)
        for idx in lst:
            ndp[idx + len(s)] = min(ndp[idx + len(s)], dp[idx + len(s)], dp[idx] + 1)
    dp = ndp

print(dp[len(T)] if dp[len(T)] != 1 << 60 else -1)
