from collections import deque
from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
x = list(map(int, readline().split()))

zero_idx = n
for i in range(n):
    if x[i] >= 0:
        zero_idx = i
        break
x.insert(zero_idx, 0)

left = max(0, zero_idx - k)
right = max(left + k, k)
ans = 1 << 60
while left <= zero_idx and right < n + 1:
    ans = min(ans, abs(x[left]) * 2 + abs(x[right]), abs(x[left]) + abs(x[right]) * 2)
    left += 1
    right += 1
print(ans)
