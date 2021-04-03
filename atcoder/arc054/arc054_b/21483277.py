#!/usr/bin/env python3
import math


def main():
    p = float(input())

    def solve(mid):
        if 1 <= p * 2 / 3 * math.log(2) * 2**(-mid / 1.5):
            return True
        else:
            return False

    def meguru_bisect(ok, ng):
        while (abs(ok - ng) > 0.00000001):
            mid = (ok + ng) / 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    start = meguru_bisect(0, p)
    print(start + p * 2**(-start / 1.5))


if __name__ == "__main__":
    main()
