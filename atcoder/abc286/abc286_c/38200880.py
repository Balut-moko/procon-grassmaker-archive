from sys import stdin
from collections import deque

readline = stdin.readline
n, a, b = map(int, readline().split())
s = deque(readline()[:-1])

ans = 1 << 60

for i in range(n):
    cnt = 0
    for j in range(n // 2):
        if s[j] != s[-j - 1]:
            cnt += 1
    ans = min(ans, i * a + cnt * b)
    val = s.popleft()
    s.append(val)
print(ans)
