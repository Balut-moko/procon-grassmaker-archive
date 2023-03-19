from sys import stdin
from collections import deque

readline = stdin.readline
L, n1, n2 = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * n1]
b = [tuple(map(int, readline().split())) for _ in [0] * n2]
que1 = deque(a)
que2 = deque(b)
ans = 0
cnt = 0

l1, r1 = 1, a[0][1]
v1 = a[0][0]
l2, r2 = 1, b[0][1]
v2 = b[0][0]
que1.popleft()
que2.popleft()

while que1 or que2:
    if v1 == v2 and max(l1, l2) <= min(r1, r2):
        ans += min(r1, r2) - max(l1, l2) + 1
    if r1 < r2:
        v, l = que1.popleft()
        v1 = v
        l1 = r1 + 1
        r1 = l1 + l - 1
    elif r2 < r1:
        v, l = que2.popleft()
        v2 = v
        l2 = r2 + 1
        r2 = l2 + l - 1
    else:
        if r1 == L:
            break
        v, l = que1.popleft()
        v1 = v
        l1 = r1 + 1
        r1 = l1 + l - 1
        v, l = que2.popleft()
        v2 = v
        l2 = r2 + 1
        r2 = l2 + l - 1

if v1 == v2 and max(l1, l2) <= min(r1, r2):
    ans += min(r1, r2) - max(l1, l2) + 1

print(ans)
