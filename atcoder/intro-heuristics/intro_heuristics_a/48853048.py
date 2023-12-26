D = int(input())
C = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in [0] * D]

csum = sum(C)


def calc_score(T: list[int]):
    last = [-1] * 26
    score, cost = 0, 0
    for d, contest in enumerate(T):
        score += S[d][contest]
        cost += csum - (d - last[contest]) * C[contest]
        last[contest] = d
        score -= cost
    return score


def evaluate(T: list[int], k):
    last = [-1] * 26
    score, cost = 0, 0
    for d, contest in enumerate(T):
        score += S[d][contest]
        cost += csum - (d - last[contest]) * C[contest]
        last[contest] = d
        score -= cost

    for d in range(len(T), min(len(T) + k, D)):
        cost += csum
        score -= cost

    return score


def solve(k):
    T = []
    for _ in range(D):
        max_score = 0
        best_i = 0
        for i in range(26):
            T.append(i)
            score = evaluate(T, k)
            if max_score < score:
                max_score = score
                best_i = i
            T.pop()
        T.append(best_i)
    return T, max_score


def solve_greedy():
    T = []
    for _ in range(D):
        max_score = 0
        best_i = 0
        for i in range(26):
            T.append(i)
            score = calc_score(T)
            if max_score < score:
                max_score = score
                best_i = i
            T.pop()
        T.append(best_i)
    return T


T = solve_greedy()
max_score = calc_score(T)
ans = T[:]
for k in range(10):
    T, score = solve(k)
    if max_score < score:
        max_score = score
        ans = T[:]

print(*[t + 1 for t in ans], sep="\n")
