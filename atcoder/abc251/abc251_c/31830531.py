from sys import stdin

readline = stdin.readline
n = int(readline())
st = [tuple(readline().split()) for _ in [0] * n]
origin_check = set()
ans = 0
point = -1
for i, val in enumerate(st):
    s, t = val
    t = int(t)
    if s not in origin_check and t > point:
        ans = i + 1
        point = t
    origin_check.add(s)

print(ans)
