from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
r, h = 0, 0
for val in s:
    if val == "o":
        r += 1
    if val == "x":
        h += 1

print("Yes" if r > 0 and h == 0 else "No")
