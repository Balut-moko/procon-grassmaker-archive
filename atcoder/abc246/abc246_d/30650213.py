from sys import stdin

readline = stdin.readline
n = int(readline())
a = 0
b = 0


def meguru_bisect(ok, ng):
    def solve(mid):
        if n <= a ** 3 + a ** 2 * mid + a * mid ** 2 + mid ** 3:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = 10 ** 18

for i in range(10 ** 6):
    b = meguru_bisect(10 ** 6, -1)
    ans = min(ans, a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3)
    a += 1

print(ans)
