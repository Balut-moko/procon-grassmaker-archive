def round_up0(p, q):
    if q < 0:
        p = -p
        q = -q
    return (p + q - 1) // q


def solve(x: int):
    global need
    n = need
    cost = x * P[3]
    n -= x
    cost += round_up0(n, 2) * P[4]
    return cost


T = int(input())

for _ in range(T):
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    need = 0
    for i, a in enumerate(A):
        need += (2 - i) * a
    if need <= 0:
        print(0)
        continue
    # ans = ternary_search_integer(0, need + 1)
    if need % 2 == 0:
        c4 = need * P[3]
        c5 = round_up0(need, 2) * P[4]
        ans = min(c4, c5)
        print(ans)
    else:
        c4 = need * P[3]
        c5 = round_up0(need, 2) * P[4]
        c45 = (need // 2) * P[4] + P[3]
        c54 = (need - 1) * P[3] + P[4]
        ans = min(c4, c5, c45, c54)
        print(ans)
