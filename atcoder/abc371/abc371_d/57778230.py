from bisect import bisect_left, bisect_right
from itertools import accumulate


N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

cs_P = list(accumulate(P, initial=0))


Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    idxL = bisect_left(X, L)
    idxR = bisect_right(X, R)
    print(cs_P[idxR] - cs_P[idxL])
