from sys import stdin
from collections import Counter
readline = stdin.readline
n = int(readline())
d = list(map(int, readline().split()))
m = int(readline())
t = list(map(int, readline().split()))
d_cnt = Counter(d)
t_cnt = Counter(t)
ans = 'YES'
for key, val in t_cnt.items():
    if d_cnt[key] < val:
        ans = 'NO'
print(ans)
