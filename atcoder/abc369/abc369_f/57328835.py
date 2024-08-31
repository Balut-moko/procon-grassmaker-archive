from functools import cmp_to_key
from atcoder.segtree import SegTree


def compare(a, b):
    if a[0] != b[0]:
        return a[0] - b[0]
    elif a[1] != b[1]:
        return a[1] - b[1]
    else:
        return 0


H, W, N = map(int, input().split())
RC = [tuple(map(int, input().split())) for _ in [0] * N]
RC.sort(key=cmp_to_key(compare))

segtree = SegTree(max, 0, 200010)
di = dict()
for r, c in RC:
    cur = segtree.prod(c, c + 1)
    nxt = segtree.prod(0, c + 1) + 1
    segtree.set(c, max(cur, nxt))
    di[(r, c)] = max(cur, nxt)

ans = segtree.prod(0, 200010)
cnt = ans
move = []
for rc in RC[::-1]:
    if di[rc] == cnt:

        move.append("R" * (W - rc[1]))
        move.append("D" * (H - rc[0]))
        W = rc[1]
        H = rc[0]
        cnt -= 1

move.append("R" * (W - 1))
move.append("D" * (H - 1))

print(ans)
print(*move[::-1], sep="")
