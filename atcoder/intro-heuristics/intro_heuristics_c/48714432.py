D = int(input())
C = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in [0] * D]
T = [int(input()) - 1 for _ in [0] * D]
M = int(input())
DQ = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * M]

csum = sum(C)


def calc_score(T):
    last = [-1] * 26
    score, cost = 0, 0
    for d in range(D):
        score += S[d][T[d]]
        cost += csum - (d - last[T[d]]) * C[T[d]]
        last[T[d]] = d
        score -= cost
    return score


for m in range(M):
    d, q = DQ[m]
    T[d] = q
    print(calc_score(T))
