from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
A = list(map(int, readline().split()))

a = 1
b = n * (n + 1) // 2

for i in range(n):
    sm = []
    lr = []
    AA = A.copy()
    for j in range(i + 1, n):
        if A[j] < A[i]:
            sm.append(A[j])
        if A[j] > A[i]:
            lr.append(A[j])
    x = -1
    if k - a < len(sm):
        sm.sort()
        x = sm[k - a]
    if b - k < len(lr):
        lr.sort(reverse=True)
        x = lr[b - k]
    if x != -1:
        j = i
        while A[j] != x:
            j += 1
        A = AA[:i] + AA[i : j + 1][::-1] + AA[j + 1 :]
        break
    a += len(sm)
    b -= len(lr)
print(*A)
