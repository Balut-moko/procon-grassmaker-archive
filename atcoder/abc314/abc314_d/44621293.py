from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
q = int(readline())
txc = [readline().split() for _ in [0] * q]
lower = None
ans = [None] * n
for i in range(q - 1, -1, -1):
    t, x, c = txc[i]
    t = int(t)
    x = int(x) - 1
    if t == 1:
        if ans[x] is None:
            if lower is None:
                ans[x] = c
            elif lower:
                ans[x] = c.lower()
            else:
                ans[x] = c.upper()
    if t == 2:
        if lower is None:
            lower = True
    if t == 3:
        if lower is None:
            lower = False

for i in range(n):
    if ans[i] is None:
        if lower is None:
            ans[i] = s[i]
        elif lower:
            ans[i] = s[i].lower()
        else:
            ans[i] = s[i].upper()

print(*ans, sep="")
