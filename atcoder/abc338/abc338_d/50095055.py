N, M = map(int, input().split())
X = list(map(lambda x: int(x) - 1, input().split()))
v = [0] * (N + 1)


def dist(pre, to):
    if pre <= to:
        return to - pre
    else:
        return to + N - pre


def add(pre, to, num):
    if pre <= to:
        v[pre] += num
        v[to] -= num
    else:
        v[pre] += num
        v[N] -= num
        v[0] += num
        v[to] -= num


for i in range(M - 1):
    add(X[i], X[i + 1], dist(X[i + 1], X[i]))
    add(X[i + 1], X[i], dist(X[i], X[i + 1]))

ans = 1 << 60
for i in range(N):
    v[i + 1] += v[i]
    ans = min(ans, v[i])
print(ans)
