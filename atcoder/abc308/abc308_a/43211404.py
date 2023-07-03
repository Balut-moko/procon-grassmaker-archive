from sys import stdin

readline = stdin.readline
s = list(map(int, readline().split()))
pre = -1
flag = True
for i in range(8):
    if not (100 <= s[i] <= 675):
        flag = not flag
        break
    if s[i] % 25 != 0:
        flag = not flag
        break
    if not (pre <= s[i]):
        flag = not flag
        break
    pre = s[i]

print("Yes" if flag else "No")
