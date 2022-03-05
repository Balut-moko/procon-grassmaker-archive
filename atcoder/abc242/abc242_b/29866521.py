from sys import stdin

readline = stdin.readline
s = sorted(readline()[:-1])
print(*s, sep="")
