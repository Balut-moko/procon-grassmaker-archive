from sys import stdin

readline = stdin.readline
s = readline()[:-1]

s = s.replace("a", "")
s = s.replace("e", "")
s = s.replace("i", "")
s = s.replace("o", "")
s = s.replace("u", "")

print(s)
