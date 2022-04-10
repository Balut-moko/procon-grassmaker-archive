from sys import stdin
from collections import defaultdict

readline = stdin.readline
n = int(readline())
st = [tuple(readline().split()) for _ in [0] * n]
d = defaultdict(int)

for si, ti in st:
    if si != ti:
        d[si] += 1
        d[ti] += 1
    else:
        d[si] += 1

flg = True
for si, ti in st:
    if d[si] == 1:
        continue
    if d[ti] == 1:
        continue
    flg = False

if flg:
    ans = "Yes"
else:
    ans = "No"
print(ans)
