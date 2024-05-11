N = int(input())
H = list(map(int, input().split()))

mx = H[0]
ans = 1
for i in range(N):
    if mx < H[i]:
        ans = i + 1
        mx = H[i]
        break


print(ans if ans != 1 else -1)
