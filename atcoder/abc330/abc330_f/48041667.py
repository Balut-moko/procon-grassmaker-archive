N, K = map(int, input().split())
X = [0] * N
Y = [0] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

X.sort()
Y.sort()


def calc(A, x):
    B = [a - x for a in A]
    AB = A + B
    AB.sort()
    med = AB[N]
    res = 0
    for i in range(N):
        if A[i] < med:
            res += med - A[i]
        elif A[i] > med + x:
            res += A[i] - (med + x)
    return res


def meguru_bisect(ok: int, ng: int):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if calc(X, mid) + calc(Y, mid) <= K:
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(1 << 60, -1))
