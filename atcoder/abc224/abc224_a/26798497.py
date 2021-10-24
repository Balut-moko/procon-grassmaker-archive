from sys import stdin

readline = stdin.readline
s = readline()[:-1]
if 'er' in s[-2:]:
    ans = 'er'
else:
    ans = 'ist'
print(ans)
