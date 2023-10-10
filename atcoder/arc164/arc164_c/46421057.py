N = int(input())
AB = [tuple(map(int, input().split())) for _ in [0] * N]

ans = 0
cnt = 0
m = 1 << 60
for a, b in AB:
    if a > b:
        ans += a
        cnt += 1
    else:
        ans += b
    m = min(m, abs(a - b))

if cnt % 2 == 1:
    ans -= m
print(ans)
