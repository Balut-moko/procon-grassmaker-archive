from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [list(readline()[:-1]) for _ in [0] * h]
a = [i for i in a if i != ['.'] * w]
a = [list(x) for x in zip(*a)]
a = [i for i in a if i != ['.'] * len(a[0])]
a = [list(x) for x in zip(*a)]
for i in a:
    print(*i, sep='')
