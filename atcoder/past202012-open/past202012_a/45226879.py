from sys import stdin

readline = stdin.readline
s = readline()[:-1]

if "ooo" in s:
    print("o")
elif "xxx" in s:
    print("x")
else:
    print("draw")
