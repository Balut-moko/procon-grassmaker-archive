#!/usr/bin/env python3

def main():
    n = int(input())
    b = 0
    c = 0

    def meguru_bisect(ok, ng):
        def solve(mid):
            # めぐる式二分探索(return boolen)
            if n < mid * (2**b):
                return False
            return True

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = 1 << 60
    while 2**b <= n:
        a = meguru_bisect(0, 10**18)
        c = n - a * (2**b)
        ans = min(ans, a + b + c)
        b += 1

    print(ans)


if __name__ == "__main__":
    main()
