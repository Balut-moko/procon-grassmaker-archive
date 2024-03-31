S = input()
ans = set()
for l in range(len(S)):
    for r in range(l + 1, len(S) + 1):
        ans.add(S[l:r])
print(len(ans))
