from sys import stdin

readline = stdin.readline
n = int(readline())

s = [readline()[:-1] for _ in [0] * n]
a, b = 0, 0
ba = 0
ans = 0
for val in s:
    if val[-1] == "A" and val[0] == "B":
        ba += 1
    elif val[-1] == "A":
        a += 1
    elif val[0] == "B":
        b += 1
    ans += val.count("AB")
if ba > 0:
    ans += ba - 1
    if a > 0:
        ans += 1
        if b > 0:
            ans += 1
            a -= 1
            b -= 1
    elif b > 0:
        ans += 1

ans += min(a, b)


print(ans)
