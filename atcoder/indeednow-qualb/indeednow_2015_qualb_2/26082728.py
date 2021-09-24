from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]
for i in range(len(s) + 1):
    if s == t:
        print(i)
        exit()
    s = s[-1] + s[:-1]
else:
    print(-1)
