from bisect import bisect_left, bisect_right
from collections import defaultdict
from sys import stdin


readline = stdin.readline
h, w, rs, cs = map(int, readline().split())
n = int(readline())
rc = [tuple(map(int, readline().split())) for _ in [0] * n]
rc.sort()
r_blocks = defaultdict(list)
for r, c in rc:
    r_blocks[r].append(c)
rc.sort(key=lambda x: x[1])
c_blocks = defaultdict(list)
for r, c in rc:
    c_blocks[c].append(r)

q = int(readline())
dl = [tuple(readline().split()) for _ in [0] * q]


def move(rs, cs, d, l):
    l = int(l)
    if d == "L":
        block_idx = bisect_left(r_blocks[rs], cs)
        if block_idx == 0:
            cs = max(cs - l, 1)
        else:
            cs = max(cs - l, r_blocks[rs][block_idx - 1] + 1)
    if d == "R":
        block_idx = bisect_left(r_blocks[rs], cs)
        if block_idx == len(r_blocks[rs]):
            cs = min(cs + l, w)
        else:
            cs = min(cs + l, r_blocks[rs][block_idx] - 1)
    if d == "U":
        block_idx = bisect_left(c_blocks[cs], rs)
        if block_idx == 0:
            rs = max(rs - l, 1)
        else:
            rs = max(rs - l, c_blocks[cs][block_idx - 1] + 1)
    if d == "D":
        block_idx = bisect_left(c_blocks[cs], rs)
        if block_idx == len(c_blocks[cs]):
            rs = min(rs + l, h)
        else:
            rs = min(rs + l, c_blocks[cs][block_idx] - 1)
    return rs, cs


for d, l in dl:
    rs, cs = move(rs, cs, d, l)
    print(rs, cs)
