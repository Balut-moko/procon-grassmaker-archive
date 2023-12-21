D = int(input())
C = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in [0] * D]


def calc_score(T):
    last = [0] * 26
    score = 0
    for i in range(D):
        score += S[i][T[i]]
        last[T[i]] = i + 1
        for j in range(26):
            score -= C[j] * (i + 1 - last[j])
    return score


max_s = [max(s) for s in S]
T = [s.index(max_s[i]) + 1 for i, s in enumerate(S)]
print(*T, sep="\n")
