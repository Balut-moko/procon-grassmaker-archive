N = int(input())
S = [input() for _ in [0] * N]
idx = -1
for i in range(1, N):
    if S[i] == S[i - 1] == "sweet":
        idx = i
        break

if idx == -1 or idx == N - 1:
    flag = True
else:
    flag = False
print("Yes" if flag else "No")
