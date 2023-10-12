N = int(input())
ans = 0
tmp = 0
for i in range(N):
    a = int(input())
    tmp += a
    if a == 0:
        ans += tmp // 2
        tmp = 0
print(ans + tmp // 2)
