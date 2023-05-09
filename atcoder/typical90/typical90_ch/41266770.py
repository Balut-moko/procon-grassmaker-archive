from sys import stdin

readline = stdin.readline
N, Q = map(int, readline().split())
req = [tuple(map(int, readline().split())) for _ in [0] * Q]
MOD = 10**9 + 7


def has_bit(n, i):
    return n & (1 << i) > 0


ans = 1
for i in range(60):
    cnt = 0
    for j in range(1 << N):
        for x, y, z, w in req:
            x -= 1
            y -= 1
            z -= 1
            if (j >> x & 1) | (j >> y & 1) | (j >> z & 1) != (w >> i & 1):
                break
        else:
            cnt += 1
    ans *= cnt
    ans %= MOD

print(ans)
