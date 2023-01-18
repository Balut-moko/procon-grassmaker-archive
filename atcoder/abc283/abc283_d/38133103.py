from sys import stdin
from collections import deque

readline = stdin.readline
s = list(readline()[:-1])
s_set = set()
que = deque([])
for i, val in enumerate(s):
    if val == "(":
        que.append(val)
    elif val == ")":
        tmp = val
        while tmp != "(":
            tmp = que.pop()
            if tmp != "(":
                s_set.remove(tmp)
    else:
        if val not in s_set:
            s_set.add(val)
            que.append(val)
        else:
            print("No")
            exit()
print("Yes")
