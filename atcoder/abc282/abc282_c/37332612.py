from sys import stdin

readline = stdin.readline
n = int(readline())
s = list(readline()[:-1])
flg = False
for i, val in enumerate(s):
    if val == '"':
        flg = not flg
    if flg == False and val == ",":
        s[i] = "."
print(*s, sep="")
