from sys import stdin

readline = stdin.readline
a, b, c, x = map(int, readline().split())

if x <= a:
    ans = 1
elif x <= b:
    ans = c / (b - a)
else:
    ans = 0
print(ans)
