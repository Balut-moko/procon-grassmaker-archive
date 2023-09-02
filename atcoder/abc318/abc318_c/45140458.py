from collections import deque
from sys import stdin

readline = stdin.readline
n, d, p = map(int, readline().split())
f = list(map(int, readline().split()))
f.sort()
que = deque(f)
tmp, cnt = 0, 0
ans = 0
while que:
    v = que.pop()
    tmp += v
    cnt += 1
    if cnt == d:
        if p <= tmp:
            ans += p
        else:
            ans += tmp
        tmp = 0
        cnt = 0
if p <= tmp:
    ans += p
else:
    ans += tmp

print(ans)
