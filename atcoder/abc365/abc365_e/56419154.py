N = int(input())
A = list(map(int, input().split()))
L = 30
cnt = [0] * L
ans = 0
for p in range(L):
    x = 0
    c = [1, 0]
    for a in A:
        x ^= (a >> p) & 1
        c[x] += 1
    ans += c[0] * c[1] << p

ans -= sum(A)
print(ans)
