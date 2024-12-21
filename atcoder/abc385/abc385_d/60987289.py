from bisect import bisect_left, bisect_right
from collections import defaultdict


N, M, Sx, Sy = map(int, input().split())

XY = [tuple(map(int, input().split())) for _ in [0] * N]
DC = [tuple(input().split()) for _ in [0] * M]
set_XY = set(XY)
x_dict = defaultdict(list)
visited_x_dict = defaultdict(list)
visited_y_dict = defaultdict(list)

for x, y in XY:
    x_dict[x].append(y)
for v in x_dict.values():
    v.sort()

for d, c in DC:
    c = int(c)
    if d == "L":
        nr, nc = Sx - c, Sy
        visited_y_dict[Sy].append((nr, Sx))
    if d == "R":
        nr, nc = Sx + c, Sy
        visited_y_dict[Sy].append((Sx, nr))
    if d == "D":
        nr, nc = Sx, Sy - c
        visited_x_dict[Sx].append((nc, Sy))
    if d == "U":
        nr, nc = Sx, Sy + c
        visited_x_dict[Sx].append((Sy, nc))
    Sx, Sy = nr, nc

ans = 0
for k, v in visited_x_dict.items():
    v.sort()
    range_list = []
    left = -1 << 60
    right = -1 << 60
    for vv in v:
        if right < vv[0]:
            if right != -1 << 60:
                range_list.append((left, right))
            left = vv[0]
        else:
            left = min(left, vv[0])
        right = max(right, vv[1])
    if not range_list:
        range_list.append((left, right))
    if range_list[-1] != (left, right):
        range_list.append((left, right))

    for l, r in range_list:
        rr = bisect_right(x_dict[k], r)
        ll = bisect_left(x_dict[k], l)
        ans += rr - ll
        for i in x_dict[k][ll:rr]:
            set_XY.discard((k, i))

y_dict = defaultdict(list)

for x, y in set_XY:
    y_dict[y].append(x)
for v in y_dict.values():
    v.sort()

for k, v in visited_y_dict.items():
    v.sort()
    range_list = []
    left = -1 << 60
    right = -1 << 60
    for vv in v:
        if right < vv[0]:
            if right != -1 << 60:
                range_list.append((left, right))
            left = vv[0]
        else:
            left = min(left, vv[0])
        right = max(right, vv[1])
    if not range_list:
        range_list.append((left, right))
    if range_list[-1] != (left, right):
        range_list.append((left, right))

    for l, r in range_list:
        rr = bisect_right(y_dict[k], r)
        ll = bisect_left(y_dict[k], l)
        ans += rr - ll

print(Sx, Sy, ans)
