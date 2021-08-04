#!/usr/bin/env python3

def main():
    n, L = map(int, input().split())
    k = int(input())
    a = list(map(int, input().split()))

    def meguru_bisect(ok, ng):
        def solve(mid):
            # めぐる式二分探索(return boolen)
            cut = 0
            tmp = 0
            for i in range(n):
                if mid <= a[i] - tmp:
                    cut += 1
                    tmp = a[i]
                if cut == k and mid <= L - tmp:
                    return True
            return False

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, 10**9 + 1))


if __name__ == "__main__":
    main()
