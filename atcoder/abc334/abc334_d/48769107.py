from bisect import bisect_right
from itertools import accumulate


N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
Rcum = list(accumulate(R, initial=0))
for _ in range(Q):
    X = int(input())
    print(bisect_right(Rcum, X) - 1)
