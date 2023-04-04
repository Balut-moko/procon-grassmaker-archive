from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = 0
for i, val in enumerate(s):
    if i % 2 == 0:
        ans += int(val)
    else:
        ans -= int(val)
print(ans)
