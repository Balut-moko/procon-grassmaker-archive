N = int(input())

lst = [i for i in range(1, N - 1)]
lst += [N, N - 1] * (N - 1) + [N]

for i in range(N - 2, 1, -2):
    lst += [i, i - 1] * (i - 2) + [i]
print(*lst)
