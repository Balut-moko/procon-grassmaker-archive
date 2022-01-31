from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]
a_trans = list(zip(*a))
sum_row = [sum(row) for row in a]
sum_col = [sum(col) for col in a_trans]
ans = [[0] * w for _ in [0] * h]

for i in range(h):
    for j in range(w):
        ans[i][j] = sum_row[i] + sum_col[j] - a[i][j]
for row in ans:
    print(*row)
