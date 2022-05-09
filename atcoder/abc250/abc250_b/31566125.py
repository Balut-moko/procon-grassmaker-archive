from sys import stdin

readline = stdin.readline
n, a, b = map(int, readline().split())
white = [[] for _ in range(a)]
black = [[] for _ in range(a)]
for aa in range(a):
    for i in range(n):
        if i % 2 == 0:
            white[aa] += "." * b
            black[aa] += "#" * b
        else:
            white[aa] += "#" * b
            black[aa] += "." * b

for i in range(n):
    if i % 2 == 0:
        for w in white:
            print(*w, sep="")
    else:
        for bl in black:
            print(*bl, sep="")
