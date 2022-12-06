from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            ans += 1
print(ans)
