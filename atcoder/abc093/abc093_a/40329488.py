from sys import stdin

readline = stdin.readline
s = readline()[:-1]
flag = True
if "a" not in s:
    flag = False
if "b" not in s:
    flag = False
if "c" not in s:
    flag = False
print("Yes" if flag else "No")
