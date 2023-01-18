from sys import stdin

readline = stdin.readline
t = int(readline())
for _ in range(t):
    n = int(readline())
    a = list(map(int, readline().split()))
    print(len([val for val in a if val % 2 == 1]))
