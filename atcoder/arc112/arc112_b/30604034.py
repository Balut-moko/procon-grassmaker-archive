from sys import stdin

readline = stdin.readline
b, c = map(int, readline().split())
l = b - c // 2
r = b
if c >= 2:
    r = b + (c - 2) // 2
b = -b
c -= 1
p = b - c // 2
q = b + c // 2
ans = r - l + 1 + q - p + 1
u = max(l, p)
v = min(r, q)
if u <= v:
    ans -= v - u + 1
print(ans)
