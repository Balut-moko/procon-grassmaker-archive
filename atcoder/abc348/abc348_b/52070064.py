def calc_dist(p, q):
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])


N = int(input())

XY = [tuple(map(int, input().split())) for _ in [0] * N]

for i in range(N):
    dist = 0
    idx = -1
    for j in range(N):
        if i == j:
            continue
        d = calc_dist(XY[i], XY[j])
        if dist < d:
            dist = d
            idx = j + 1
    print(idx)
