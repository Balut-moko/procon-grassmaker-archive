from sys import stdin

readline = stdin.readline
x, y = map(int, readline().split('.'))
if 0 <= y <= 2:
    ans = '-'
elif 2 < y <= 6:
    ans = ''
else:
    ans = '+'
print(str(x) + ans)
