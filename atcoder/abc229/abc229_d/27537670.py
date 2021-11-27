from sys import stdin
from collections import deque

readline = stdin.readline
s = readline()[:-1]
k = int(readline())
q = deque()
ans = 0
cnt = 0
for val in s:
    q.append(val)
    if val == '.':
        cnt += 1
    while q and cnt > k:
        tmp = q.popleft()
        if tmp == '.':
            cnt -= 1
    ans = max(ans, len(q))

print(ans)
