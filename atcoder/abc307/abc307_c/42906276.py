from itertools import product
from sys import stdin

readline = stdin.readline
ha, wa = map(int, readline().split())
a = [readline()[:-1] for _ in [0] * ha]
a_cnt = 0
for i in range(ha):
    for j in range(wa):
        if a[i][j] == "#":
            a_cnt += 1

hb, wb = map(int, readline().split())
b = [readline()[:-1] for _ in [0] * hb]
b_cnt = 0
for i in range(hb):
    for j in range(wb):
        if b[i][j] == "#":
            b_cnt += 1

hx, wx = map(int, readline().split())
x = [readline()[:-1] for _ in [0] * hx]

ans = "No"
for ai, aj, bi, bj in product(
    range(-hx, hx), range(-wx, wx), range(-hx, hx), range(-wx, wx)
):
    a_tmp, b_tmp = 0, 0
    for i in range(hx):
        for j in range(wx):
            if x[i][j] == ".":
                continue
            flag = False
            if 0 <= i - ai < ha and 0 <= j - aj < wa:
                if a[i - ai][j - aj] == "#":
                    a_tmp += 1
                    flag = True
            if 0 <= i - bi < hb and 0 <= j - bj < wb:
                if b[i - bi][j - bj] == "#":
                    b_tmp += 1
                    flag = True
            if not flag:
                break
        else:
            continue
        break
    else:
        if a_cnt == a_tmp and b_cnt == b_tmp:
            ans = "Yes"

print(ans)
