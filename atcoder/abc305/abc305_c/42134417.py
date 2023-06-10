from sys import stdin

readline = stdin.readline
H, W = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * H]
sr = list(zip(*s))
mr, mc = 0, 0
for i in range(H):
    if "#" not in s[i]:
        continue
    cnt = s[i].count("#")
    mr = max(mr, cnt)

for i in range(H):
    if "#" not in s[i]:
        continue
    cnt = s[i].count("#")
    if cnt != mr:
        ans_i = i + 1

for j in range(W):
    if "#" not in sr[j]:
        continue
    cnt = sr[j].count("#")
    mc = max(mc, cnt)

for j in range(W):
    if "#" not in sr[j]:
        continue
    cnt = sr[j].count("#")
    if cnt != mc:
        ans_j = j + 1

print(ans_i, ans_j)
