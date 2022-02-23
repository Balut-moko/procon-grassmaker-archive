from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_sum = sum(a)

a += a
ans = "No"
cnt = 0
q = deque()
for val in a:
    q.append(val)
    cnt += val
    while q and not (cnt * 10 <= a_sum):  # (満たすべき条件)
        rm = q.popleft()
        cnt -= rm
    if cnt * 10 == a_sum:
        ans = "Yes"

print(ans)
