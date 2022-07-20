from sys import stdin

readline = stdin.readline
s = readline()[:-1]

if s.count(s[0]) == 1:
    print(s[0])
elif s.count(s[1]) == 1:
    print(s[1])
elif s.count(s[2]) == 1:
    print(s[2])
else:
    print(-1)
