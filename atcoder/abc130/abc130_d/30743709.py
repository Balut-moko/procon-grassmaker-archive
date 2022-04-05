from sys import stdin
from collections import deque

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

ans = 0
sum_a = 0
q = deque()
for i, val in enumerate(a):
    q.append(val)
    sum_a += val
    while q and k <= sum_a:
        rm = q.popleft()
        sum_a -= rm
        ans += n - i

print(ans)
