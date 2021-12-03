from sys import stdin

readline = stdin.readline
n = int(readline())
if n >= 42:
    n += 1
ans = 'AGC' + str(n).zfill(3)
print(ans)
