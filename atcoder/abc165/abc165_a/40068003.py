from sys import stdin

readline = stdin.readline
k = int(readline())
a, b = map(int, readline().split())
flag = False
for i in range(a, b + 1):
    if i % k == 0:
        flag = True
print("OK" if flag else "NG")
