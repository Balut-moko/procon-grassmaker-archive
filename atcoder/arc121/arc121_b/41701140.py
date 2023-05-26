from bisect import bisect_left
from sys import stdin

readline = stdin.readline
n = int(readline())
rl, gl, bl = [], [], []
for i in range(2 * n):
    a, c = readline().split()
    a = int(a)
    if c == "R":
        rl.append(a)
    elif c == "G":
        gl.append(a)
    else:
        bl.append(a)
rl.sort()
gl.sort()
bl.sort()

if len(rl) % 2 == len(gl) % 2 == len(bl) % 2 == 0:
    print(0)
    exit()

if len(gl) % 2 == len(bl) % 2 == 1:
    rl, bl = bl, rl

if len(bl) % 2 == len(rl) % 2 == 1:
    gl, bl = bl, gl


def calc_min(l1, l2):
    res = 1 << 60
    if len(l2) == 0:
        return res
    for val in l1:
        idx = bisect_left(l2, val)
        if idx == 0:
            tmp = l2[idx] - val
        elif idx == len(l2):
            tmp = val - l2[idx - 1]
        else:
            tmp = min(l2[idx] - val, val - l2[idx - 1])
        res = min(res, tmp)
    return res


ans = min(calc_min(rl, gl), calc_min(gl, bl) + calc_min(rl, bl))
print(ans)
