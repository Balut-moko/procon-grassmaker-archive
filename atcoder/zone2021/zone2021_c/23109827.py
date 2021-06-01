#!/usr/bin/env python3
import itertools


def main():
    n = int(input())
    power = [list(map(int, input().split())) for _ in range(n)]

    def meguru_bisect(ok, ng):
        def solve(mid):
            # めぐる式二分探索(return boolen)
            tmp_power = set()
            for p in power:
                tmp_power.add(tuple([1 if mid <= a else 0 for a in p]))
            tmp_power = list(tmp_power)
            for val in itertools.combinations_with_replacement(tmp_power, 3):
                tmp = [0] * 5
                for v in val:
                    tmp = list(map(sum, zip(tmp, v)))
                if min(tmp) != 0:
                    return True
            return False

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, 10 ** 9 + 1))


if __name__ == "__main__":
    main()
