from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

cnt = 0
ans = deque()
for i in range(n):
    ans.append(s[i])
    if s[i] == "(":
        cnt += 1
    if s[i] == ")":
        if cnt > 0:
            val = ""
            while val != "(":
                val = ans.pop()
            cnt -= 1
print("".join(ans))
