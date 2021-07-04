from sys import stdin
from math import factorial

readline = stdin.readline
p = int(readline())
i = 10
ans = 0
while 0 < p:
    ans += p // factorial(i)
    p %= factorial(i)
    i -= 1
print(ans)
