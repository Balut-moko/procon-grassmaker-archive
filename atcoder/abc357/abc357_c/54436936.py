from functools import cache


@cache
def calc(level, i, j):
    if level == 0:
        return "#"
    level -= 1
    if 3**level <= i < 2 * 3**level and 3**level <= j < 2 * 3**level:
        return "."

    return calc(level, i % (3**level), j % (3**level))


N = int(input())

ans = [["#"] * 3**N for _ in range(3**N)]

for i in range(3**N):
    for j in range(3**N):
        ans[i][j] = calc(N, i, j)

for val in ans:
    print(*val, sep="")
