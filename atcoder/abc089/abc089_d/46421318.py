H, W, D = map(int, input().split())
grid = [input().split() for _ in [0] * H]

di = dict()
for i in range(H):
    for j in range(W):
        di[int(grid[i][j])] = (i, j)


cost = [0] * (H * W + 1)


def calc_cost(s, t):
    i, j = di[s]
    x, y = di[t]
    return abs(x - i) + abs(y - j)


for d in range(1, D + 1):
    i, j = di[d]
    pre = d
    nd = d + D
    while nd <= H * W:
        c = calc_cost(pre, nd)
        cost[nd] = cost[pre] + c
        pre = nd
        nd += D


q = int(input())

for _ in range(q):
    L, R = map(int, input().split())
    print(cost[R] - cost[L])
