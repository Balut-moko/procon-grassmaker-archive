N = int(input())
WX = [tuple(map(int, input().split())) for _ in [0] * N]

ans = 0

for i in range(24):
    tmp = 0
    for w, x in WX:
        t = (x + i) % 24
        if 9 <= t < 18:
            tmp += w
    ans = max(ans, tmp)

print(ans)
