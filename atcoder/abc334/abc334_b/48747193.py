A, M, L, R = map(int, input().split())


def round_up0(p, q):
    if q < 0:
        p = -p
        q = -q
    return (p + q - 1) // q


L_cnt = round_up0(L - A, M)
R_cnt = (R - A) // M

print(R_cnt - L_cnt + 1)
