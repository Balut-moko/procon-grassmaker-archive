from itertools import combinations
from sys import stdin


def check(p4):
    dist = []
    for i in range(4):
        for j in range(i + 1, 4):
            dx = p4[i][0] - p4[j][0]
            dy = p4[i][1] - p4[j][1]
            dist.append(dx * dx + dy * dy)
    dist.sort()
    l = dist[0]
    return (
        dist[0] == l
        and dist[1] == l
        and dist[2] == l
        and dist[3] == l
        and dist[4] == l * 2
        and dist[5] == l * 2
    )


readline = stdin.readline
s = [readline()[:-1] for _ in range(9)]
points = []
for i in range(9):
    for j in range(9):
        if s[i][j] == "#":
            points.append((i, j))

ans = 0
for p4 in combinations(points, 4):
    if check(p4):
        ans += 1

print(ans)
