#!/usr/bin/env python3
import bisect


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    def meguru_bisect(ok, ng, k):
        def solve(mid):
            idx = bisect.bisect_left(a, mid)
            if mid - idx <= k:
                return True
            return False
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok
    for i in range(q):
        k = int(input())
        print(meguru_bisect(0, 10**19, k))


if __name__ == "__main__":
    main()
