from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

di = defaultdict(list)

for i in range(N):
    di[A[i]].append(W[i])

ans = 0
for lst in di.values():
    lst.sort(reverse=True)
    while len(lst) > 1:
        ans += lst.pop()

print(ans)
