from sys import stdin

readline = stdin.readline
n, d = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]

cnt = [0]*d

for i in range(n):
    for j in range(d):
        if s[i][j] == "x":
            cnt[j] += 1
ans = 0
tmp = 0
for j in range(d):
    if cnt[j] == 0:
        tmp += 1
    else:
        tmp = 0
    ans = max(ans,tmp)
print(ans)