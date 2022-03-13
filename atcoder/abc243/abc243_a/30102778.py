from sys import stdin

readline = stdin.readline
v, a, b, c = map(int, readline().split())

while 0 <= v:
    v -= a
    if v < 0:
        ans = "F"
        break
    v -= b
    if v < 0:
        ans = "M"
        break
    v -= c
    if v < 0:
        ans = "T"
        break
print(ans)
