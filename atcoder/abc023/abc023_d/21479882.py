#!/usr/bin/env python3
import itertools


def main():
    n = int(input())
    hs_li = [list(map(int, input().split())) for _ in range(n)]

    def solve(mid):
        cnt = [0] * n
        for hs in hs_li:
            if mid < hs[0]:
                return False
            else:
                tmp = (mid - hs[0]) // hs[1]
                if tmp < n:
                    cnt[tmp] += 1
        cum = list(itertools.accumulate(cnt, initial=0))
        for i in range(n):
            if i < cum[i]:
                return False
        return True

    def meguru_bisect(ok, ng):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(1 << 60, 0))


if __name__ == "__main__":
    main()
