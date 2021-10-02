from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]
if s == t:
    print('Yes')
    exit()
for i in range(len(s) - 1):
    tmp = s[:i] + s[i + 1] + s[i] + s[i + 2:]
    if tmp == t:
        print('Yes')
        exit()
print('No')
