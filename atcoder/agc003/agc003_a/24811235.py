from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = 'Yes'
if 'N' in s:
    if 'S' not in s:
        ans = 'No'
else:
    if 'S' in s:
        ans = 'No'
if 'E' in s:
    if 'W' not in s:
        ans = 'No'
else:
    if 'W' in s:
        ans = 'No'

print(ans)
