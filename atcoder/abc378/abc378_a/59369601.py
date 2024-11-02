from collections import defaultdict


A = list(map(int, input().split()))
di = defaultdict(int)
for a in A:
    di[a] += 1
ans = 0
for v in di.values():
    ans += v // 2
print(ans)
