from sys import stdin

readline = stdin.readline
a, b, c = map(int, readline().split())
if a < c**b:
    ans = "Yes"
else:
    ans = "No"
print(ans)
