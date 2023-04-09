from sys import stdin

readline = stdin.readline
s = readline()[:-1]
bl = -1
rl = -1
for i, val in enumerate(s):
    if val == "B":
        if bl == -1:
            bl = i
        else:
            br = i
    if val == "R":
        if rl == -1:
            rl = i
        else:
            rr = i
    if val == "K":
        k = i

flag = True
if bl % 2 == br % 2:
    flag = False

if not (rl < k < rr):
    flag = False

print("Yes" if flag else "No")
