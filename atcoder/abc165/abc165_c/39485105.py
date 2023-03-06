from sys import stdin
from itertools import combinations_with_replacement

readline = stdin.readline
n, m, q = map(int, readline().split())
abcd = [tuple(map(int, readline().split())) for _ in [0] * q]
ans = 0
for nums in combinations_with_replacement(range(1, m + 1), n):
    tmp = 0
    for a, b, c, d in abcd:
        if nums[b - 1] - nums[a - 1] == c:
            tmp += d
    ans = max(ans, tmp)
print(ans)
