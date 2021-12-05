from sys import stdin

readline = stdin.readline
a = int(readline())
b = int(readline())

if b % 2 == 0:
    tmp = b // 2
else:
    tmp = (b * 10) // 2
ans = str(a) + "0" + str(tmp)
print(ans)
