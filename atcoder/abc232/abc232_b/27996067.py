from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]
atoz = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
for k in range(26):
    for i in range(len(s)):
        if atoz[atoz.index(s[i]) + k] != t[i]:
            break
    else:
        print('Yes')
        exit()
print('No')
