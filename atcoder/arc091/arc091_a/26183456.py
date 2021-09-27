from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
if n == 1 and m == 1:
    ans = 1
elif n == 1 or m == 1:
    ans = n * m - 2
else:
    ans = n * m - (n * 2 + m * 2 - 4)
print(ans)
