from sys import stdin
from collections import defaultdict
readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
color = defaultdict(int)
over = 0
for val in a:
    if val // 400 < 8:
        color[val // 400] += 1
    else:
        over += 1

print(max(1, len(color)), len(color) + over)
