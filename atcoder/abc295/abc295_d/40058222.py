from sys import stdin
from collections import defaultdict

readline = stdin.readline
s = readline()[:-1]

flags = [False] * 10

di = defaultdict(int)
di[tuple(flags)] += 1

for val in s:
    flags[int(val)] = not flags[int(val)]
    di[tuple(flags)] += 1

ans = 0
for val in di.values():
    ans += val*(val-1)//2
print(ans)