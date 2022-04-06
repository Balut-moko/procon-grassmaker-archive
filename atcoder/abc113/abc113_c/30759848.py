from sys import stdin
from collections import defaultdict

readline = stdin.readline
n, m = map(int, readline().split())
py = []
for i in range(m):
    p, y = map(int, readline().split())
    py.append([i, p, y])

py_sorted = sorted(py, key=lambda x: x[2])
p_dict = defaultdict(int)

ans = [""] * m
for i, p, y in py_sorted:
    p_dict[p] += 1
    ans[i] = str(p).zfill(6) + str(p_dict[p]).zfill(6)

print(*ans, sep="\n")
