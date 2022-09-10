from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))


def calc_point(idx):
    tmp_p = p[n - idx :] + p[: n - idx]
    point = [0] * n
    for i, val in enumerate(tmp_p):
        tmp = (val - i) % n
        point[val] = min(tmp, n - tmp)
    return sum(point)


ans = 1 << 60

l, r = 0, n - 1
while l + 2 < r:
    c1 = l + (r - l) // 3
    c2 = r - (r - l) // 3
    if calc_point(c1) < calc_point(c2):
        r = c2
    else:
        l = c1

ans = min(ans, calc_point(l), calc_point(l + 1), calc_point(r))

l, r = n // 2, n - 1
while l + 2 < r:
    c1 = l + (r - l) // 3
    c2 = r - (r - l) // 3
    if calc_point(c1) < calc_point(c2):
        r = c2
    else:
        l = c1

ans = min(ans, calc_point(l), calc_point(l + 1), calc_point(r))

l, r = 0, n // 2
while l + 2 < r:
    c1 = l + (r - l) // 3
    c2 = r - (r - l) // 3
    if calc_point(c1) < calc_point(c2):
        r = c2
    else:
        l = c1

ans = min(ans, calc_point(l), calc_point(l + 1), calc_point(r))
print(ans)
