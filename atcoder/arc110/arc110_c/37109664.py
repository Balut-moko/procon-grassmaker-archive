from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(lambda x: int(x) - 1, readline().split()))
p_idx = [0] * n
for i, val in enumerate(p):
    p_idx[val] = i
num = 0
ans = []
while num != n - 1:
    idx = p_idx[num]
    if idx == num:
        num += 1
        continue
    for i in range(idx, num, -1):
        p[i - 1], p[i] = p[i], p[i - 1]
        p_idx[p[i - 1]], p_idx[p[i]] = i - 1, i
        ans.append(i)

    for i in range(num, idx):
        if p[i] != i:
            print(-1)
            exit()
    num = idx

for i in range(n):
    if p[i]!=i:
        print(-1)
        exit()

if len(ans) == n - 1:
    print(*ans, sep="\n")
else:
    print(-1)
