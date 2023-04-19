from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
cd = [tuple(map(int, readline().split())) for _ in [0] * m]


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        mon = []
        for a, b in ab:
            mon.append(b - a * mid)
        mon_m = -1 << 60
        for c, d in cd:
            mon_m = max(mon_m, d - c * mid)
        mon.append(mon_m)
        mon.sort()
        return sum(mon[-5:]) >= 0

    for _ in range(100):
        mid = (ok + ng) / 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 1 << 60))
