from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
if s[n - 1] == 'o':
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
