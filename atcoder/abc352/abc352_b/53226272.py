S = input()
T = input()

ans = []
idx = 0
for i in range(len(T)):
    if S[idx] == T[i]:
        ans.append(i + 1)
        idx += 1

print(*ans)
