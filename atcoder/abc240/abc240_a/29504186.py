from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
if b - a == 1 or (a == 1 and b == 10):
    ans = "Yes"
else:
    ans = "No"
print(ans)
