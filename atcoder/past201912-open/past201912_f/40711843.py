from curses.ascii import isupper
from sys import stdin

readline = stdin.readline
s = readline()[:-1]

lst = []
flag = False
for i, val in enumerate(s):
    if not flag and val.isupper():
        flag = True
        left = i
    elif flag and val.isupper():
        flag = False
        lst.append(s[left : i + 1])

print(*sorted(lst, key=lambda x: x.lower()), sep="")
