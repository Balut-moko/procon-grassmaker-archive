from bisect import bisect_left, bisect_right


N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))
zero = []
set0 = set()
set1 = set()
for i in range(N):
    if S[i] == "0":
        zero.append(X[i] - T)
        zero.append(X[i])
        set0.add((X[i] - T, X[i]))
    else:
        set1.add((X[i], X[i] + T))
zero.sort()
ans = 0
for i in range(N):
    if S[i] == "1":
        l = bisect_left(zero, X[i])
        r = bisect_right(zero, X[i] + T)
        ans += r - l

set01 = set0 & set1
print(ans - len(set01))
