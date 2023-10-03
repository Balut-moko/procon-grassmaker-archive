from itertools import product


polyomino = [[] * 4 for _ in range(3)]
for i in range(3):
    for j in range(4):
        s = list(input())
        polyomino[i].append(s)

cnt = 0
for i in range(3):
    for j in range(4):
        for k in range(4):
            if polyomino[i][j][k] == "#":
                cnt += 1
if cnt != 16:
    print("No")
    exit()


def check(ps, mino, grid):
    res = [[0] * 10 for i in range(10)]
    for j in range(4):
        for k in range(4):
            res[j + 3][k + 3] = grid[j + 3][k + 3]
    for j in range(4):
        for k in range(4):
            if mino[j][k] == "#":
                if 3 <= j + ps[0] < 7 and 3 <= k + ps[1] < 7:
                    if grid[j + ps[0]][k + ps[1]] == 0:
                        res[j + ps[0]][k + ps[1]] = 1
                    else:
                        return False, res
                else:
                    return False, res
    return True, res


for rotate in product(range(4), repeat=3):
    minos = []
    for i, r in enumerate(rotate):
        tmp = polyomino[i]
        for _ in range(r):
            tmp = [x for x in zip(*tmp[::-1])]
        minos.append(tmp)

    for p1 in product(range(7), repeat=2):
        grid = [[0] * 10 for i in range(10)]
        flag, grid1 = check(p1, minos[0], grid)
        if flag:
            for p2 in product(range(7), repeat=2):
                flag, grid2 = check(p2, minos[1], grid1)
                if flag:
                    for p3 in product(range(7), repeat=2):
                        flag, grid3 = check(p3, minos[2], grid2)
                        if flag:
                            print("Yes")
                            exit()
print("No")
