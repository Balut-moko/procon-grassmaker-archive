from sys import stdin


def score(a, b):
    res = 0
    for i, val in enumerate(a):
        res += abs(val - (b + i + 1))
    return res


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

l, r = -1 << 60, 1 << 60

while l + 2 < r:
    c1 = l + (r - l) // 3
    c2 = r - (r - l) // 3
    if score(a, c1) < score(a, c2):
        r = c2
    else:
        l = c1

ans = min(score(a, l), score(a, l + 1), score(a, l + 2))
print(ans)
