from collections import deque
from sys import stdin

readline = stdin.readline
x = readline()[:-1]

que = deque()

for val in x:
    if not que:
        que.append(val)
        continue
    if val == "T" and que[-1] == "S":
        que.pop()
        continue
    que.append(val)
print(len(que))
