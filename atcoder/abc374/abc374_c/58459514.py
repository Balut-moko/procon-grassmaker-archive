from bisect import bisect_left


N = int(input())
K = list(map(int, input().split()))
K.sort(reverse=True)

A = K[: N // 2]
B = K[N // 2 :]

AS = {0}
for a in A:
    tmp = AS.copy()
    for t in tmp:
        AS.add(a + t)
BS = {0}
for b in B:
    tmp = BS.copy()
    for t in tmp:
        BS.add(b + t)

sum_K = sum(K)
AL = sorted(AS)
BL = sorted(BS) + [sum_K]

ans = sum_K
for a in AL:
    tmp = (sum_K + 1) // 2
    idx = bisect_left(BL, tmp - a)
    ans = min(ans, a + BL[idx])

print(ans)
