from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = ''
for val in s:
    if val != 'B':
        ans += val
    elif ans != '':
        ans = ans[:-1]
print(ans)
