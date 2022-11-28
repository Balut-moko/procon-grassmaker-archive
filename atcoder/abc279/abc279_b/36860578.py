from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]

print("Yes" if t in s else "No")
