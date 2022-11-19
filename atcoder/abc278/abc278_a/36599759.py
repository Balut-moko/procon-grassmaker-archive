from collections import deque
from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
que = deque(a)

for _ in range(k):
    que.popleft()
    que.append(0)

print(*que)
