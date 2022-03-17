from sys import stdin


def manhattan_dist(p1, p2):
    dist = 0
    for a, b in zip(p1, p2):
        dist += abs(a - b)
    return dist


readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]

xy.sort()
x_median = xy[n // 2][0]

xy.sort(key=lambda x: x[1])
y_median = xy[n // 2][1]

ans = 0

for x, y in xy:
    ans += manhattan_dist((x, y), (x_median, y_median))

print(ans)
