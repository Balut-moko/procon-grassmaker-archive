from collections import deque
from sys import stdin


readline = stdin.readline
n, x, y = map(int, readline().split())
que_red = deque([(n, 1)])
que_blue = deque([])
ans = 0

while que_red:
    level, cnt = que_red.popleft()
    if level > 1:
        que_red.append([level - 1, cnt])
        que_blue.append([level, x * cnt])
    while que_blue:
        level_b, cnt_b = que_blue.popleft()
        if level_b > 1:
            que_red.append([level_b - 1, cnt_b])
            que_blue.append([level_b - 1, y * cnt_b])
        else:
            ans += cnt_b

print(ans)
