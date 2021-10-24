from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]
ans = 'Yes'
for i1 in range(h):
    for i2 in range(i1, h):
        for j1 in range(w):
            for j2 in range(j1, w):
                if a[i1][j1] + a[i2][j2] > a[i2][j1] + a[i1][j2]:
                    ans = 'No'
print(ans)
