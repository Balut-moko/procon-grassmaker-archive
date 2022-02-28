from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

s = s.replace("A", "BB")
s = s.replace("BB", "A")
print(s)
