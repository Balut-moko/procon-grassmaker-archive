from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

l = s.find("|")
r = s.rfind("|")

if "*" in s[l:r]:
    print("in")
else:
    print("out")
