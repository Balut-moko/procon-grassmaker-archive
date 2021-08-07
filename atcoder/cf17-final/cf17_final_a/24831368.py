from sys import stdin

readline = stdin.readline()
s = readline[:-1]
ans = 'YES'
i = 0
for c in 'AKIHABARA':
    if i < len(s) and c == s[i]:
        i += 1
    elif c != 'A':
        ans = 'NO'
if i != len(s):
    ans = 'NO'
print(ans)
