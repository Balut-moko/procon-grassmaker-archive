from sys import stdin
from collections import deque, defaultdict

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

ans = 0
val_di = defaultdict(int)
cnt = 0

q = deque()
for val in a:
    q.append(val)
    val_di[val] += 1
    if val_di[val] == 1:
        cnt += 1
    while q and not (cnt <= k):  # (満たすべき条件)
        rm = q.popleft()
        val_di[rm] -= 1
        if val_di[rm] == 0:
            cnt -= 1
    ans = max(ans, len(q))

print(ans)
