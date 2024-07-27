from bisect import bisect_left, bisect_right


def solve(mid: int):
    left = bisect_left(A, b - mid)
    right = bisect_right(A, b + mid)
    return right - left >= k


def meguru_bisect(ok: int, ng: int):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, Q = map(int, input().split())
A = sorted(map(int, input().split()))

for _ in range(Q):
    b, k = map(int, input().split())
    print(meguru_bisect(1 << 60, -1))
