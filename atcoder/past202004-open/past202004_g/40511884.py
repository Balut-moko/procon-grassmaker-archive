from collections import deque
from sys import stdin

readline = stdin.readline
Q = int(readline())
que = deque([])

for _ in range(Q):
    t, *q = readline().split()
    if t == "1":
        c, x = q
        x = int(x)
        que.append([c, x])
    if t == "2":
        cnt = [0] * 26
        d = int(q[0])
        while d and que:
            c, x = que.popleft()
            if d < x:
                x -= d
                que.appendleft([c, x])
                cnt[ord(c) - ord("a")] += d
                d = 0
            else:
                cnt[ord(c) - ord("a")] += x
                d -= x
        ans = 0
        for val in cnt:
            ans += val * val
        print(ans)
