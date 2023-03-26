from sys import stdin

readline = stdin.readline
n = int(readline())
i = 0
while n:
    i += 1
    if str(i).count(str(i)[0]) == len(str(i)):
        n -= 1

print(i)
