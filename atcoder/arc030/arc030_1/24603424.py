from sys import stdin

readline = stdin.readline

n = int(readline())
k = int(readline())
if k <= n // 2:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)
