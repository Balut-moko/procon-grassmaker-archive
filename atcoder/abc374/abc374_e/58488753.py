N, X = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * N]


def calc(a, p, b, q, W):
    cost = 1 << 60
    for i in range(b + 1):
        w = W
        w -= a * i
        c = p * i
        c += q * max(0, (w + b - 1) // b)
        cost = min(cost, c)
    for i in range(a + 1):
        w = W
        w -= b * i
        c = q * i
        c += p * max(0, (w + a - 1) // a)
        cost = min(cost, c)

    return cost


def solve(mid: int):
    cost = sum(calc(a, p, b, q, mid) for a, p, b, q in A)
    return cost <= X


def meguru_bisect(ok: int, ng: int):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 1 << 60))
