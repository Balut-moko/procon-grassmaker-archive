from collections import defaultdict


S = input()

cnt = defaultdict(int)
for s in S:
    cnt[s] += 1

if cnt["1"] == 1 and cnt["2"] == 2 and cnt["3"] == 3:
    print("Yes")
else:
    print("No")
