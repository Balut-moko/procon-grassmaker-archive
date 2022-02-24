from sys import stdin


def meguru_bisect(ok, ng, pieces, k):
    def solve(mid, pieces, k):
        cnt = 0
        length = 0
        for val in pieces:
            length += val
            if mid <= length:
                cnt += 1
                length = 0
        if k + 1 <= cnt:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid, pieces, k):
            ok = mid
        else:
            ng = mid
    return ok


readline = stdin.readline
n, l = map(int, readline().split())
k = int(readline())
a = [0] + list(map(int, readline().split())) + [l]
pieces = [a[i + 1] - a[i] for i in range(n + 1)]

print(meguru_bisect(1, 10**9 + 1, pieces, k))
