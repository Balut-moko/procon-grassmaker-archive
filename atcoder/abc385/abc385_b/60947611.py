H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1

S = [input() for _ in [0] * H]
T = input()

visited = [[False] * W for _ in [0] * H]
ans = 0
for t in T:
    if t == "U":
        nr, nc = X - 1, Y
    if t == "D":
        nr, nc = X + 1, Y
    if t == "L":
        nr, nc = X, Y - 1
    if t == "R":
        nr, nc = X, Y + 1
    if not (0 <= nr < H and 0 <= nc < W) or S[nr][nc] == "#":
        continue
    if S[nr][nc] == "@" and not visited[nr][nc]:
        visited[nr][nc] = True
        ans += 1
    X, Y = nr, nc

print(X + 1, Y + 1, ans)
