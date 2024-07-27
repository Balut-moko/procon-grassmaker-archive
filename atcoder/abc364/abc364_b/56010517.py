H, W = map(int, input().split())
si, sj = map(lambda x: int(x) - 1, input().split())

C = [tuple(input()) for _ in [0] * H]
X = input()
dd = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

for x in X:
    ni = si + dd[x][0]
    nj = sj + dd[x][1]
    if not (0 <= ni < H and 0 <= nj < W) or C[ni][nj] == "#":
        continue
    si, sj = ni, nj

print(si + 1, sj + 1)
