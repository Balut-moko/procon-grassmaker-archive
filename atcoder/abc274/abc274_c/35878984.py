from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

ameba = [None] * (2 * n + 2)
ameba[1] = 0
for i in range(1, n + 1):
    gene = ameba[a[i - 1]]
    ameba[2 * i] = gene + 1
    ameba[2 * i + 1] = gene + 1

print(*ameba[1:], sep="\n")
