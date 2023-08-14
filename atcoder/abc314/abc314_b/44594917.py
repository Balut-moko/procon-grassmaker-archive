from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
di = defaultdict(lambda: defaultdict(set))
for i in range(n):
    c = int(readline())
    a = list(map(int, readline().split()))
    for j in range(c):
        di[a[j]][c].add(i + 1)
x = int(readline())

ans= []

for c in range(1,38):
    if di[x][c]:
        ans = list(di[x][c])
        break

if len(ans):
    print(len(ans))
    print(*ans)
else:
    print(0)