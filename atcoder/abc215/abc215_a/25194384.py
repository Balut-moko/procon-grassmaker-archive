from sys import stdin

readline = stdin.readline
if readline()[:-1] == 'Hello,World!':
    ans = 'AC'
else:
    ans = 'WA'
print(ans)
