from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
if 0 < a and b == 0:
    ans = 'Gold'
elif a == 0 and 0 < b:
    ans = 'Silver'
else:
    ans = 'Alloy'
print(ans)
