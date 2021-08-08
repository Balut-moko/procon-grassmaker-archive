from sys import stdin


readline = stdin.readline
h, w, n = map(int, readline().split())
ab = []
for i in range(n):
    a, b = map(int, readline().split())
    ab.append([a, b, i + 1])

ab_sorted = sorted(ab)
tmp = ab_sorted[0][0]
ab_sorted[0][0] = 1
cnt = 1
for i in range(1, n):
    if ab_sorted[i][0] != tmp:
        cnt += 1
    tmp = ab_sorted[i][0]
    ab_sorted[i][0] = cnt

ab_sorted = sorted(ab, key=lambda x: x[1])
tmp = ab_sorted[0][1]
ab_sorted[0][1] = 1
cnt = 1
for i in range(1, n):
    if ab_sorted[i][1] != tmp:
        cnt += 1
    tmp = ab_sorted[i][1]
    ab_sorted[i][1] = cnt

ab_sorted = sorted(ab, key=lambda x: x[2])
for i in range(n):
    print(ab_sorted[i][0], ab_sorted[i][1])
