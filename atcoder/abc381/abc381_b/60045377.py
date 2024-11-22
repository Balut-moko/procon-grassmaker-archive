from collections import Counter


S = input()

cnt = Counter(S)

for c in "abcdefghijklmnopqrstuvwxyz":
    if cnt[c] == 0 or cnt[c] == 2:
        continue
    print("No")
    exit()

for i in range(len(S) // 2):
    if S[i * 2] != S[i * 2 + 1]:
        print("No")
        exit()

print("Yes")
