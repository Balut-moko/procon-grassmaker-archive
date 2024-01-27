from collections import defaultdict


S = input()
di = defaultdict(int)

for s in S:
    di[s] += 1

items = sorted(di.items())
cnt = 0
for k, v in items:
    if cnt < v:
        ans = k
        cnt = v

print(ans)
