from sys import stdin

readline = stdin.readline
s = readline()[:-1]
flag = False
if s in ("ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"):
    flag = True


print("Yes" if flag else "No")
