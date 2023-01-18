from sys import stdin
from collections import deque

readline = stdin.readline
s = list(readline()[:-1])
que = deque(s)
ans = 0
cnt = 0
while que:
    val = que.popleft()
    if val != "0":
        ans += (cnt + 1) // 2
        cnt = 0
        ans += 1
    else:
        cnt += 1
ans += (cnt + 1) // 2
print(ans)
