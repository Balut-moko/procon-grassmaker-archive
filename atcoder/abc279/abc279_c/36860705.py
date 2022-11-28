from collections import defaultdict
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
t = [readline()[:-1] for _ in [0] * h]

s = list(zip(*s))
t = list(zip(*t))

di = defaultdict(int)

for val in t:
    di[val] += 1

flag = True
for val in s:
    di[val] -= 1
    if di[val] < 0:
        flag = False
print("Yes" if flag else "No")
