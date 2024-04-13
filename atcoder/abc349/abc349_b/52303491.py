from collections import defaultdict
from string import ascii_lowercase


S = input()
di = defaultdict(set)
for c in ascii_lowercase:
    cnt = S.count(c)
    di[cnt].add(c)
flag = True
for i in range(1, 101):
    if len(di[i]) == 0 or len(di[i]) == 2:
        continue
    flag = False

print("Yes" if flag else "No")
