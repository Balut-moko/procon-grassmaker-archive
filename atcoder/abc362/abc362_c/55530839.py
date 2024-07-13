N = int(input())
LR = [tuple(map(int, input().split())) for _ in [0] * N]

mn = sum(l for l, r in LR)
mx = sum(r for l, r in LR)

if 0 < mn or mx < 0:
    print("No")
    exit()

ans = []
for l, r in LR:
    if mn < 0:
        if r - l < -mn:
            ans.append(r)
            mn += r - l
        else:
            ans.append(l - mn)
            mn = 0
    else:
        ans.append(l)

print("Yes")
print(*ans)
