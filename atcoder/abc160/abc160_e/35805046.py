from collections import deque
from sys import stdin

readline = stdin.readline
x, y, a, b, c = map(int, readline().split())
p = list(map(int, readline().split()))
q = list(map(int, readline().split()))
r = list(map(int, readline().split()))
p.sort(reverse=True)
q.sort(reverse=True)

pp = p[:x]
qq = q[:y]
pqr = sorted(pp + qq + r, reverse=True)
ans = sum(pqr[: x + y])
print(ans)
