from itertools import combinations
from bisect import bisect_right

N, K, P = map(int, input().split())
A = list(map(int, input().split()))
L, R = A[: N // 2], A[N // 2 :]
L_list = []
R_list = []
for k in range(K + 1):
    L_list.append(sorted(sum(v) for v in combinations(L, k)))
    R_list.append(sorted(sum(v) for v in combinations(R, k)))

ans = 0
for i, ll in enumerate(L_list):
    if len(R_list) < K - i + 1:
        break
    for lv in ll:
        ans += bisect_right(R_list[K - i], P - lv)

print(ans)
