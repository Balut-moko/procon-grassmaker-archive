from collections import deque


N, Q = map(int, input().split())

que = []
for i in range(N, 0, -1):
    que.append((i, 0))
dd = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
hx, hy = 1, 0

for _ in range(Q):
    num, c = input().split()
    if num == "1":
        dx, dy = dd[c]
        hx += dx
        hy += dy
        que.append((hx, hy))
    else:
        p = int(c)
        print(*que[-p])
