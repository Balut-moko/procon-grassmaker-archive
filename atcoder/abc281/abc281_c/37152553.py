from sys import stdin

readline = stdin.readline
n, t = map(int, readline().split())
a = list(map(int, readline().split()))

sum_a = sum(a)

t %= sum_a

for i, val in enumerate(a):
    if t < val:
        print(i + 1, t)
        exit()
    t -= val
