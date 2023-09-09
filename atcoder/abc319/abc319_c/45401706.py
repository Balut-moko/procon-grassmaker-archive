from itertools import permutations
from sys import stdin

readline = stdin.readline
c = [tuple(map(int, readline().split())) for _ in [0] * 3]

ij = ((i, j) for i in range(3) for j in range(3))


def check():
    cr = (used[0][0], used[1][1], used[2][2])
    if cr.count(None) == 1 and len(set(cr)) == 2:
        return True
    cr = (used[0][2], used[1][1], used[2][0])
    if cr.count(None) == 1 and len(set(cr)) == 2:
        return True
    for i in range(3):
        if used[i].count(None) == 1 and len(set(used[i])) == 2:
            return True
    for j in range(3):
        col = (used[0][j], used[1][j], used[2][j])
        if col.count(None) == 1 and len(set(col)) == 2:
            return True
    return False


cnt = 0

for val in permutations(ij):
    used = [[None, None, None], [None, None, None], [None, None, None]]
    for i, j in val:
        used[i][j] = c[i][j]
        if check():
            cnt += 1
            break
print(1 - cnt / (9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1))
