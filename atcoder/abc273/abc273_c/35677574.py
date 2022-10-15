from sys import stdin
from bisect import bisect_right

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_set = set(a)
kinds = len(a_set)
sorted_a = sorted(a_set)
ans = [0] * (n + 1)
for i, val in enumerate(a):
    idx = bisect_right(sorted_a, val)
    ans[kinds - idx] += 1
print(*ans[:-1], sep="\n")
