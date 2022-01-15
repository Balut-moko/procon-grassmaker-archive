from sys import stdin
from collections import deque

readline = stdin.readline
a, n = map(int, readline().split())
num_li = [1 << 60] * 10**6
num_li[1] = 0
que = deque()
que.append(1)
while que:
    x = que.popleft()
    if x == n:
        break

    nxt_x = x * a
    if nxt_x < 10**6:
        if num_li[nxt_x] > num_li[x] + 1:
            num_li[nxt_x] = num_li[x] + 1
            que.append(nxt_x)

    if x >= 10 and x % 10 != 0:
        x_str = str(x)
        nxt_x = int(x_str[-1] + x_str[:-1])
        if nxt_x < 10**6:
            if num_li[nxt_x] > num_li[x] + 1:
                num_li[nxt_x] = num_li[x] + 1
                que.append(nxt_x)

print(num_li[n] if num_li[n] != 1 << 60 else -1)
