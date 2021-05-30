#!/usr/bin/env python3
def main():
    n, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    def meguru_bisect(ok, ng):
        def solve(mid):
            cnt_li = [[0] * n for _ in range(n)]
            s = [[0] * (n + 1) for _ in range(n + 1)]

            for i in range(n):
                for j in range(n):
                    if mid < A[i][j]:
                        cnt_li[i][j] = 1
            for i in range(n):
                for j in range(n):
                    s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + cnt_li[i][j]
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    if s[i + k][j + k] - s[i][j + k] - s[i + k][j] + s[i][j] < ((k * k) // 2) + 1:
                        return True
            return False
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(10**9, -1))


if __name__ == "__main__":
    main()
