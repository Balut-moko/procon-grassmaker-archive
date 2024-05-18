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


def has_bit(n, i):
    return n & (1 << i) > 0


@lru_cache(maxsize=None)
def rec(flag, turn):
    for i in range(N):
        if has_bit(flag, i):
            continue
        for v in pairs[i]:
            if has_bit(flag, v):
                continue
            nxt = flag
            nxt += 1 << i
            nxt += 1 << v
            if rec(nxt, turn ^ 1) == turn:
                return turn
    return turn ^ 1


print(["Takahashi", "Aoki"][rec(0, 0)])
