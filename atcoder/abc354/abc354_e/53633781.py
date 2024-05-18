from collections import defaultdict
from functools import lru_cache

N = int(input())
AB = [tuple(map(int, input().split())) for _ in [0] * N]

pairs = defaultdict(tuple)

for i in range(N):
    for j in range(i + 1, N):
        if AB[i][0] == AB[j][0] or AB[i][1] == AB[j][1]:
            tmp = list(pairs[i])
            tmp.append(j)
            pairs[i] = tuple(tmp)


@lru_cache(maxsize=None)
def rec(used, turn):
    for i in range(N):
        if used[i] == 1:
            continue
        for v in pairs[i]:
            if used[v] == 1:
                continue
            nxt = list(used)
            nxt[i] = 1
            nxt[v] = 1
            if rec(tuple(nxt), turn ^ 1) == turn:
                return turn
    return turn ^ 1


print(["Takahashi", "Aoki"][rec((0,) * N, 0)])
