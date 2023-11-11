N = int(input())
D = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(1, D[i] + 1):
        if len(set(list(str(i + 1))) | set(list(str(j)))) == 1:
            ans += 1
print(ans)
