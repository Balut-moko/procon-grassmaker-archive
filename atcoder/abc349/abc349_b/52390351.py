from collections import Counter

S = input()
cnt1 = Counter(S)
cnt2 = Counter(cnt1.values())

print("Yes" if all(c == 2 for c in cnt2.values()) else "No")
