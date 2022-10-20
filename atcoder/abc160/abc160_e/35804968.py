from collections import deque
from sys import stdin

readline = stdin.readline
x, y, a, b, c = map(int, readline().split())
p = list(map(int, readline().split()))
q = list(map(int, readline().split()))
r = list(map(int, readline().split()))
p.sort()
q.sort()
r.sort()

pp = p[a - x :]
qq = q[b - y :]
pq = sorted(pp + qq)
ans = sum(pq)
que = deque(pq)
que_blank = deque(r)
while que:
    if not que_blank:
        break
    tmp = que.popleft()
    if tmp < que_blank[-1]:
        tt = que_blank.pop()
        ans += tt - tmp
print(ans)
