from sys import stdin

readline = stdin.readline
n = int(readline())
flag = False
for i in range(0, 101, 5):
    if abs(n - i) <= 2:
        ans = i
        break
print(ans)
