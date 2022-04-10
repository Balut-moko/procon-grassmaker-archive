from sys import stdin
from collections import deque, defaultdict

readline = stdin.readline
q = int(readline())
query = [tuple(map(int, readline().split())) for _ in [0] * q]
que = deque([])

for q in query:
    if q[0] == 1:
        d = defaultdict(int)
        d[q[1]] = q[2]
        que.append(d)
    else:
        c = q[1]
        cnt = 0
        while c != 0:
            d = que.popleft()
            key, val = [[k, v] for k, v in d.items()][0]
            if val >= c:
                d[key] -= c
                cnt += key * c
                que.appendleft(d)
                break
            else:
                cnt += key * val
                c -= val
        print(cnt)
