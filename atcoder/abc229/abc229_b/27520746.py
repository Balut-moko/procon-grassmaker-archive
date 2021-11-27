from sys import stdin

readline = stdin.readline
a, b = readline().split()
ans = 'Easy'
digit = min(len(a), len(b))
for i in range(digit):
    if int(a[-1 - i]) + int(b[-1 - i]) >= 10:
        ans = 'Hard'
print(ans)
