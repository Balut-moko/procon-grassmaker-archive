N, M, K = map(int, input().split())

C = []
A = []
R = []

for i in range(M):
    c, *a, r = input().split()
    c = int(c)
    a = list(map(lambda x: int(x) - 1, a))
    C.append(c)
    A.append(a)
    R.append(True if r == "o" else False)


def has_bit(n, i):
    return n & (1 << i) > 0


ALL = 1 << N
ans = 0
for n in range(ALL):
    for i in range(M):
        cnt = 0
        for j in range(C[i]):
            if has_bit(n, A[i][j]):
                cnt += 1
        if (K <= cnt) ^ R[i]:
            break
    else:
        ans += 1

print(ans)
