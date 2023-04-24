from sys import stdin


def rotate_45_degrees(x, y):
    return x - y, x + y


readline = stdin.readline
n, q = map(int, readline().split())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]
rotated = [(rotate_45_degrees(x, y)) for x, y in xy]
max_x = -1 << 60
max_y = -1 << 60
min_x = 1 << 60
min_y = 1 << 60
for x, y in rotated:
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

for _ in range(q):
    p = int(readline()) - 1
    print(
        max(
            abs(rotated[p][0] - max_x),
            abs(rotated[p][0] - min_x),
            abs(rotated[p][1] - max_y),
            abs(rotated[p][1] - min_y),
        )
    )
