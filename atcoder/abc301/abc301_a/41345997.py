from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
t = 0
a = 0
for i in range(n):
    if s[i] == "T":
        t += 1
    else:
        a += 1

if t == a:
    if s[i] == "T":
        ans = "A"
    else:
        ans = "T"

elif t < a:
    ans = "A"
else:
    ans = "T"
print(ans)
