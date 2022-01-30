from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline())
S = readline()[:-1]
S = S[::-1]
ans = deque([n])
n -= 1
for s in S:
    if s == "L":
        ans.append(n)
    else:
        ans.appendleft(n)
    n -= 1

print(*ans)
