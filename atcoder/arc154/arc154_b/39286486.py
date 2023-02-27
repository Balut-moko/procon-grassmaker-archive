from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
t = readline()[:-1]

ss = sorted(s)
ts = sorted(t)

if ss != ts:
    print(-1)
    exit()


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        idx = -1
        for i in range(mid, n):
            for j in range(idx + 1, n):
                if s[i] == t[j]:
                    idx = j
                    break
            else:
                return False
        return True

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(n, -1))
