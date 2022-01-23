from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = list(readline().split())
t = set(readline().split())

for i in range(n):
    if s[i] in t:
        print("Yes")
    else:
        print("No")
