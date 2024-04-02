def has_bit(n, i):
    return n & (1 << i) > 0


N, D = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for n in range(1 << N):
    bit = 0
    cond = 0
    for i in range(N):
        if has_bit(n, i):
            bit |= A[i]
            cond += 1
    free = 0
    for i in range(D):
        if not has_bit(bit, i):
            free += 1
    if cond % 2 == 0:
        ans += 1 << free
    else:
        ans -= 1 << free

print(ans)
