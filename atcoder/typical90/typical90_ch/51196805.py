def has_bit(n, i):
    return n & (1 << i) > 0


def check(n, i):
    for x, y, z, w in A:
        x -= 1
        y -= 1
        z -= 1
        if has_bit(n, x) | has_bit(n, y) | has_bit(n, z) != has_bit(w, i):
            return False
    return True


N, Q = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * Q]
MOD = 10**9 + 7
ans = 1
for i in range(60):
    tmp = 0
    for n in range(1 << N):
        if check(n, i):
            tmp += 1
    ans *= tmp
    ans %= MOD

print(ans)
