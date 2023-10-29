N, C = map(int, input().split())
TA = [tuple(map(int, input().split())) for _ in [0] * N]


def has_bit(n, i):
    return n & (1 << i) > 0


ans = [0] * N
for k in range(30):
    func = [0, 1]
    cur = has_bit(C, k)

    for i, v in enumerate(TA):
        t, a = v
        f = [0, 1]
        x = has_bit(a, k)
        if t == 1:
            f = [0 & x, 1 & x]
        if t == 2:
            f = [0 | x, 1 | x]
        if t == 3:
            f = [0 ^ x, 1 ^ x]
        func = [f[func[0]], f[func[1]]]
        cur = func[cur]
        ans[i] |= cur << k

print(*ans, sep="\n")
