from collections import deque
from sys import stdin
import re


readline = stdin.readline
n = int(readline())
s = readline()[:-1]

li = re.findall(r"A+RC+", s)
que = deque([])
for val in li:
    tmp = min(val.count("A"), val.count("C"))
    if tmp == 1:
        que.append(tmp)
    else:
        que.appendleft(tmp)
i = 1
ans = 0
while que:
    if i % 2 == 1:
        cnt = que.popleft()
        ans += 1
        cnt -= 1
        if cnt > 1:
            que.appendleft(cnt)
        elif cnt == 1:
            que.append(cnt)
    else:
        que.pop()
        ans += 1
    i += 1
print(ans)
