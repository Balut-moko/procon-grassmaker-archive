from sys import stdin

readline = stdin.readline
s, t = readline().split()
if s < t:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
