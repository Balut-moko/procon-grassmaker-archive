from itertools import combinations_with_replacement, product


def calc(C):
    return (C[3] - C[0]) * (C[4] - C[1]) * (C[5] - C[2])


def create(C1, C2):
    a1 = max(C1[0], C2[0])
    a2 = min(C1[3], C2[3])
    if not a1 <= a2:
        return 0, 0, 0, 0, 0, 0
    b1 = max(C1[1], C2[1])
    b2 = min(C1[4], C2[4])
    if not b1 <= b2:
        return 0, 0, 0, 0, 0, 0
    c1 = max(C1[2], C2[2])
    c2 = min(C1[5], C2[5])
    if not c1 <= c2:
        return 0, 0, 0, 0, 0, 0
    return a1, b1, c1, a2, b2, c2


V1, V2, V3 = map(int, input().split())
c1 = (0, 0, 0, 7, 7, 7)
for c2 in combinations_with_replacement(range(8), 3):
    c2 = list(c2) + list(map(lambda x: int(x) + 7, c2))
    for c3 in product(range(-7, 8), repeat=3):
        c3 = list(c3) + list(map(lambda x: int(x) + 7, c3))
        v2 = 0

        c12 = create(c1, c2)
        v2 += calc(c12)

        c23 = create(c2, c3)
        v2 += calc(c23)

        c31 = create(c3, c1)
        v2 += calc(c31)

        c123 = create(c12, c3)
        v3 = calc(c123)
        v2 -= v3 * 3
        v1 = 7 * 7 * 7 * 3 - v2 * 2 - v3 * 3

        if (v1, v2, v3) == (V1, V2, V3):
            print("Yes")
            ans = list(c1[:3]) + list(c2[:3]) + list(c3[:3])
            print(*ans)
            exit()
print("No")
