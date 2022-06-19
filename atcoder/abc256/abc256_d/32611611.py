from sys import stdin

readline = stdin.readline
n = int(readline())
lr = [tuple(map(int, readline().split())) for _ in [0] * n]

imos_li = [0] * (2 * 10 ** 5 + 1)
for l, r in lr:
    imos_li[l] += 1
    imos_li[r] -= 1

imos_cumsum = [0] * (2 * 10 ** 5 + 1)
left = -1
ans = []
for i in range(1, 2 * 10 ** 5 + 1):
    imos_cumsum[i] = imos_cumsum[i - 1] + imos_li[i]
    if imos_cumsum[i] != 0 and left == -1:
        left = i
    if imos_cumsum[i] == 0 and left != -1:
        right = i
        ans.append((left, right))
        left = -1

for val in ans:
    print(*val)
