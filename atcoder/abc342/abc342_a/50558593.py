from collections import Counter


S = input()

cnt = Counter(S)

a = cnt.most_common()[1][0]

print(S.index(a) + 1)
