from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

di = defaultdict(int)

for val in a:
    di[val] += 1
cnt1, cnt2 = 0, 0
for k, v in di.items():
    if v % 2 == 1:
        cnt1 += 1
    else:
        cnt2 += 1

while cnt2:
    if cnt2 >= 2:
        cnt2 -= 2
        cnt1 += 2
    elif cnt2 == 1:
        cnt2 = 0

print(cnt1)
