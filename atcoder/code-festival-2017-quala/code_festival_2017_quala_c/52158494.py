H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
cnt = [0] * 26

for i in range(H):
    for j in range(W):
        cnt[ord(A[i][j]) - ord("a")] += 1

g1 = (H % 2) * (W % 2)
g2 = (H // 2) * (W % 2) + (W // 2) * (H % 2)
g3 = (H // 2) * (W // 2)

for _ in range(g1):
    for a in range(26):
        if cnt[a] % 2 == 1:
            cnt[a] -= 1
            break

for _ in range(g3):
    for a in range(26):
        if cnt[a] > 0 and cnt[a] >= 4:
            cnt[a] -= 4
            break

for _ in range(g2):
    for a in range(26):
        if cnt[a] > 0 and cnt[a] % 2 == 0:
            cnt[a] -= 2
            break

ans = "Yes"
for a in range(26):
    if cnt[a] != 0:
        ans = "No"
print(ans)
