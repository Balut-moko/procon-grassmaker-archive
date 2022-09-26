from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        tmp = 0
        for val in a:
            tmp += min(val, mid)
        if tmp <= k:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


cycle = meguru_bisect(0, 10 ** 13)

for i in range(n):
    k -= min(a[i], cycle)
    a[i] -= min(a[i], cycle)
i = 0
while k > 0:
    if a[i]:
        a[i] -= 1
        k -= 1
    i += 1
    i %= n

print(*a)
