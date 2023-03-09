from itertools import product
from sys import stdin

readline = stdin.readline
n = int(readline())
xyh = [tuple(map(int, readline().split())) for _ in [0] * n]
for cx, cy in product(range(101), range(101)):

    def meguru_bisect(ok: int, ng: int):
        def solve(mid: int):
            for x, y, h in xyh:
                if h <= max(mid - abs(x - cx) - abs(y - cy), 0):
                    continue
                return False
            return True

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans_h = meguru_bisect(10**18, 0)
    for x, y, h in xyh:
        if h != max(ans_h - abs(x - cx) - abs(y - cy), 0):
            break
    else:
        print(cx, cy, ans_h)
        exit()
