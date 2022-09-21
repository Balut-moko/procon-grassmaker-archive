from sys import stdin

readline = stdin.readline
s = [readline()[:-1] for _ in [0] * 10]
a, b = 10, 1
c, d = 10, 1

for i in range(10):
    for j in range(10):
        try:
            ct = s[i].index("#")
            dt = s[i][::-1].index("#")
        except Exception:
            continue
        a = min(a, i + 1)
        b = max(b, i + 1)
        c = min(c, ct + 1)
        d = max(d, 10 - dt)
print(a, b)
print(c, d)
