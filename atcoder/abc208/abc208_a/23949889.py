from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
if a <= b <= a * 6:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
