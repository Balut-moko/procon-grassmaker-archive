from sys import stdin

readline = stdin.readline

n = int(readline())
n_set = set(range(1, 2 * n + 2))
for i in range(n + 1):
    num = n_set.pop()
    print(num, flush=True)
    num = int(readline())
    if num == 0:
        exit()
    n_set.remove(num)
