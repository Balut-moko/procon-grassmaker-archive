from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
que = deque(a)
flg = False
while que:
    if flg ^ que[-1] == 0:
        que.pop()
    elif flg ^ que[0] == 0:
        que.popleft()
        flg = not flg
    else:
        break

if que:
    ans = "No"
else:
    ans = "Yes"
print(ans)
