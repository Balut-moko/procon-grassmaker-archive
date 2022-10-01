from collections import defaultdict
from sys import stdin

readline = stdin.readline
n, s = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

di = defaultdict(str)
di[0] = ""
for i in range(n):
    items = list(di.items())
    di.clear()
    for key,val in items:
        di[key+ab[i][0]] = val+"H"
        di[key+ab[i][1]] = val+"T"

for key,val in di.items():
    if key == s:
        print("Yes")
        print(val)
        exit()
print("No")