N = int(input())
S = input()
ans = 0
for i in range(N):
    ans += 2**i * (ord(S[i]) - ord("a"))

print(ans)
