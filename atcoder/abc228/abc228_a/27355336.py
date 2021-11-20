from sys import stdin

readline = stdin.readline
s, t, x = map(int, readline().split())
if s < t:
    if s <= x < t:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    if s <= x < 24 or 0 <= x < t:
        ans = 'Yes'
    else:
        ans = 'No'
print(ans)
