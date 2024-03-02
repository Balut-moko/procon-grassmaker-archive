from itertools import combinations_with_replacement, product


def calc2(a1, b1, c1, a2, b2, c2):
    res = 1
    res *= max(0, min(a1, a2) + 7 - max(a1, a2))
    res *= max(0, min(b1, b2) + 7 - max(b1, b2))
    res *= max(0, min(c1, c2) + 7 - max(c1, c2))
    return res


def calc3(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    res = 1
    res *= max(0, min(a1, a2, a3) + 7 - max(a1, a2, a3))
    res *= max(0, min(b1, b2, b3) + 7 - max(b1, b2, b3))
    res *= max(0, min(c1, c2, c3) + 7 - max(c1, c2, c3))
    return res


V1, V2, V3 = map(int, input().split())
if V1 + V2 * 2 + V3 * 3 != 7 * 7 * 7 * 3:
    print("No")
    exit()
a1, b1, c1 = 0, 0, 0
for val in combinations_with_replacement(range(8), 3):
    a2, b2, c2 = val
    tmp = calc2(a1, b1, c1, a2, b2, c2)
    for val2 in product(range(-7, 8), repeat=3):
        a3, b3, c3 = val2
        v3 = calc3(a1, b1, c1, a2, b2, c2, a3, b3, c3)
        v2 = tmp
        v2 += calc2(a2, b2, c2, a3, b3, c3)
        v2 += calc2(a3, b3, c3, a1, b1, c1)
        v2 -= v3 * 3
        v1 = 7 * 7 * 7 * 3 - v2 * 2 - v3 * 3

        if v1 == V1 and v2 == V2 and v3 == V3:
            print("Yes")
            print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
            exit()
