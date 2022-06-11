from sys import stdin


readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(lambda x: int(x) - 1, readline().split()))
xy = [[i] + list(map(int, readline().split())) for i in range(n)]
ans = 0


def meguru_bisect(ok, ng):
    def solve(mid):
        flg = [False] * n
        for ak in a:
            _, xk, yk = xy[ak]
            for i, x, y in xy:
                if (x - xk) ** 2 + (y - yk) ** 2 <= mid:
                    flg[i] = True
        return True if sum(flg) == n else False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(1 << 60, -1) ** 0.5)
