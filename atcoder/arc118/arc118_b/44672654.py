from sys import stdin

readline = stdin.readline
k, n, m = map(int, readline().split())
a = list(map(int, readline().split()))


def check(x):
    L, R = 0, 0
    for i in range(k):
        L += max(0, (m * a[i] - x + n - 1) // n)
        R += (m * a[i] + x) // n
    return L <= m <= R


def construct(x):
    B = []
    R = []
    for i in range(k):
        B.append(max(0, (m * a[i] - x + n - 1) // n))
        R.append((m * a[i] + x) // n)
    B_sum = sum(B)
    for i in range(k):
        v = min(m - B_sum, R[i] - B[i])
        B[i] += v
        B_sum += v
    return B


ok, ng = n * m, -1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

B = construct(ok)
print(*B)
