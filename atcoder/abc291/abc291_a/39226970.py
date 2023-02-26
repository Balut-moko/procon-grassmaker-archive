from sys import stdin

readline = stdin.readline
s = readline()[:-1]

for i in range(len(s)):
    if s[i].isupper():
        print(i + 1)
