from sys import stdin

readline = stdin.readline
n = int(readline())
ans = 0
while 2**ans <= n:
    ans += 1
print(ans - 1)
