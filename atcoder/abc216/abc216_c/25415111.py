from sys import stdin

readline = stdin.readline
n = int(readline())
ans = ''
while 0 < n:
    if n % 2 == 1:
        ans += 'A'
        n -= 1
    else:
        ans += 'B'
        n //= 2

print(ans[::-1])
