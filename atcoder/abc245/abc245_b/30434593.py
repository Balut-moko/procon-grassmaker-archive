from sys import stdin

readline = stdin.readline
n = int(readline())
a = set(map(int, readline().split()))

for i in range(2001):
    if i not in a:
        print(i)
        break
