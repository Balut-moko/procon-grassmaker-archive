from sys import stdin


def que(arg):
    print(f"? {arg}", flush=True)
    return int(readline())


readline = stdin.readline
n = int(readline())


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        return que(mid) == 0

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(f"! {meguru_bisect(1, n)}")
