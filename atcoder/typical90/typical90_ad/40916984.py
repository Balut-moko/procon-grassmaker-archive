from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
cnt = [0] * (n + 1)

for i in range(2, n + 1):
    if cnt[i] != 0:
        continue
    for j in range(i, n + 1, i):
        cnt[j] += 1
print(sum(1 for val in cnt if val >= k))
