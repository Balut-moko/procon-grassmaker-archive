from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
x = int(readline())
sum_a = sum(a)
div, mod = divmod(x, sum_a)
for i in range(n):
    mod -= a[i]
    if mod < 0:
        print(div * n + i + 1)
        exit()
